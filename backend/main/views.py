from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from django.shortcuts import get_object_or_404
from django.core.signing import BadSignature
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.authtoken.models import Token

from .permission import IsOwner
from .models import (
    Packet,
    Bouquet,
    Card,
    Subscriber,
    Settings,
    LogsCard,
    LogsSubscriber,
    LogsReseller,
    reset_password,
)
from .serializer import (
    ResellerCreateSerializer,
    ResellerListSerializer,
    ResellerDetailSerializer,
    PackageListSerializer,
    PackageDetailSerializer,
    PackageCreateSerializer,
    PackageDeleteSerializer,
    PackageEditSerializer,
    CardSerializer,
    CardCreateSerializer,
    CardDetailSerializer,
    CardUpdateExpiredSerializer,
    CardSuspendSubscribtionSerializer,
    SubscriberSerializer,
    SubscriberDetailSerializer,
    SubscriberEditCardsSerializer,
    SubscriberEditBalanceSerializer,
    SubscriberCreateSerializer,
    PasswordRequestSerializer,
    PasswordSerializer,
    BouquetShortDescriptionSerializer,
    SettingsSerializer,
)
from .utilities import signer
from .api import Command


def logging(class_, instance, text, *args):
    try:
        getattr(class_, 'card')
        log = class_.objects.create(card=instance)
        log.log = text.format(log.date, instance.id, *args)
        log.save()
    except AttributeError:
        pass

    try:
        getattr(class_, 'subscriber')
        log = class_.objects.create(subscriber=instance)
        log.log = text.format(log.date, instance.id, *args)
        log.save()
    except AttributeError:
        pass

    try:
        getattr(class_, 'reseller')
        log = class_.objects.create(reseller=instance)
        log.log = text.format(log.date, instance.id, *args)
        log.save()
    except AttributeError:
        pass


User = get_user_model()


class TokenCreateView(APIView):
    """Login"""
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        token = Token.objects.filter(user=user)
        if token.exists():
            return Response({'auth_token': token.first().key, 'is_superuser': user.is_superuser})
        else:
            if user.check_password(password) and user.is_activated:
                token = Token.objects.create(user=user)
                return Response({'auth_token': token.key, 'is_superuser': user.is_superuser})
            else:
                return Response({'errors': 'Invalid data'})


class TokenDestroyView(APIView):
    """Logout"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({"message": "Logout"}, status=HTTP_200_OK)


class ResellerRegisterAPIView(generics.CreateAPIView):
    """Register Reseller"""
    permission_classes = [AllowAny]
    serializer_class = ResellerCreateSerializer
    queryset = User.objects.all()


class ResellerActivateAPIView(generics.GenericAPIView):
    """Confirm user"""
    permission_classes = [AllowAny]

    def get(self, request, sign):
        try:
            email = signer.unsign(sign)
        except BadSignature:
            return Response({'errors': 'Badsignature'})
        user = get_object_or_404(User, email=email)
        if user.is_activated:
            return Response({'errors': 'User is activated'})
        else:
            user.is_active = True
            user.is_activated = True
            user.save()
            log = 'DATE: {}; ID RESELLER: {}; LOG: Registered;'
            logging(LogsReseller, user, log)
            serializer = ResellerDetailSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)


class ResellerListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ResellerListSerializer
    queryset = User.objects.all()


class ResellerDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ResellerDetailSerializer


class ResellerEditView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ResellerDetailSerializer


class PackageListView(generics.ListAPIView):
    """Show list of Packages"""
    permission_classes = [IsAuthenticated]
    serializer_class = PackageListSerializer
    queryset = Packet.objects.all()


class PackageFilterListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PackageListSerializer
    queryset = Packet.objects.all()

    def get(self, request, *args, **kwargs):
        card = Card.objects.get(pk=kwargs['pk'])
        packages = Packet.objects.all().difference(card.packages.all())
        serializer = self.get_serializer(packages, many=True)
        return Response(serializer.data)


class PackageDetailView(generics.RetrieveAPIView):
    """Detail of package"""
    queryset = Packet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PackageDetailSerializer


class PackageCreateView(generics.CreateAPIView):
    """Add package"""
    permission_classes = [IsAdminUser]
    serializer_class = PackageCreateSerializer
    queryset = Packet.objects.all()


class PackageDeleteView(generics.DestroyAPIView):
    """Delete package"""
    permission_classes = [IsAdminUser]
    serializer_class = PackageDeleteSerializer
    queryset = Packet.objects.all()


class PackageEditView(generics.UpdateAPIView):
    """Edit package"""
    permission_classes = [IsAdminUser]
    serializer_class = PackageEditSerializer
    queryset = Packet.objects.all()


class CardListView(generics.ListAPIView):
    """Show list of Cards for owner"""
    queryset = Card.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardSerializer


class CardCreateView(generics.CreateAPIView):
    """Create a Card"""
    permission_classes = [IsAdminUser]
    serializer_class = CardCreateSerializer
    queryset = Card.objects.all()

    def create(self, request, *args, **kwargs):
        pk = Card.objects.aggregate(maxpk=models.Max('pk'))['maxpk']
        card, created = Card.objects.get_or_create(pk=pk+1)
        print(card, created)
        if created:
            log = 'DATE: {}; ID CARD: {}; LOG: Created card;'
            logging(LogsCard, card, log)
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data, status=HTTP_201_CREATED)


class CreateRangeCardView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CardCreateSerializer

    def get(self, request, *args, **kwargs):
        max_pk = Card.objects.aggregate(max_pk=models.Max('pk'))['max_pk']
        return Response({'start': max_pk + 1})

    def create(self, request, *args, **kwargs):
        start = request.data.get('start')
        stop = request.data.get('stop')
        created_cards = []
        for i in range(start, stop + 1):
            card, created = Card.objects.get_or_create(pk=i)
            if created:
                created_cards.append(card)
                log = 'DATE: {}; ID CARD: {}; LOG: Created card;'
                logging(LogsCard, card, log)
        serializer = self.get_serializer(created_cards, many=True)
        return Response(serializer.data, status=HTTP_201_CREATED)


class CardDetailView(generics.RetrieveAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardDetailSerializer
    queryset = Card.objects.all()


class CardUpdateExpiredView(generics.UpdateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardUpdateExpiredSerializer
    queryset = Card.objects.all()

    def put(self, request, *args, **kwargs):
        period = int(request.data.get('period'))

        if period <= 0:
            return Response({'detail': 'Period cannot equal to 0 or less 0'},
                            status=HTTP_400_BAD_REQUEST)

        settings = Settings.objects.first()
        card = Card.objects.get(pk=kwargs['pk'])

        if card.status() == 'Inactive' or card.status() == 'Suspend':
            return Response({'errors': 'Cannot update expired date'})

        quantity = settings.quantity
        total_period = period * quantity

        if settings.kind_payment == 'PREPAYMENT':
            if settings.kind_period == 'MONTHS':
                card.expired_date = datetime.now() + relativedelta(months=total_period)
            elif settings.kind_period == 'WEEKS':
                card.expired_date = datetime.now() + relativedelta(weeks=total_period)
            elif settings.kind_period == 'DAYS':
                card.expired_date = datetime.now() + relativedelta(days=total_period)
        else:
            return Response({'detail': 'Cannot renew subscription'},
                            status=HTTP_400_BAD_REQUEST)

        card.save(update_fields=['expired_date'])
        log = 'DATE: {}; ID CARD: {}; LOG: Update expired date {};'
        logging(LogsCard, card, log, card.expired_date)
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data)


class CardForceUpdatePackageView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardSerializer

    def put(self, request, *args, **kwargs):
        settings = Settings.objects.first()
        card = Card.objects.get(pk=kwargs['pk'])
        old_price = card.price()
        cardPackages = card.packages.all()
        data = list(cardPackages)
        package_pk = request.data.get('package')
        package = Packet.objects.filter(pk=int(package_pk))
        if package.first() is None:
            return Response({'detail': 'Cannot add this package'},
                            status=HTTP_400_BAD_REQUEST)
        data.append(package.first())
        card.packages.set(data)
        card.save()
        new_price = card.price()
        if settings.kind_payment == 'VIRTUAL':
            subscriber = card.subscriber
            diff = new_price - old_price
            if subscriber.balance - diff >= 0:
                subscriber.balance -= diff
                subscriber.save()
            else:
                return Response({'errors': 'Not enough money in the account'})
        log = 'DATE: {}; ID CARD: {}; LOG: Add package {};'
        logging(LogsCard, card, log, package.first().header)
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data)


class CardRemovePackageView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardSerializer

    def put(self, request, **kwargs):
        pk = kwargs['pk']
        card = Card.objects.get(pk=pk)
        cardPackages = card.packages.all()
        data = list(cardPackages)
        package_pk = request.data.get('package')
        package = Packet.objects.filter(pk=int(package_pk))
        if package.first() is None:
            return Response({'detail': 'Cannot remove this package'},
                            status=HTTP_400_BAD_REQUEST)
        data.remove(package.first())
        card.packages.set(data)
        card.save()
        log = 'DATE: {}; ID CARD: {}; LOG: Remove package {};'
        logging(LogsCard, card, log, package.first().header)
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data)


class CardDeleteView(generics.DestroyAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CardSerializer

    def delete(self, request, *args, **kwargs):
        card = Card.objects.get(pk=kwargs['pk'])
        if card.delete_date() > datetime.now():
            log = 'DATE: {}; ID CARD: {}; LOG: Remove card;'
            logging(LogsCard, card, log)
            card.delete()
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data)


class SubscriberListView(generics.ListAPIView):
    """Show subscribers"""
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            subscribers = self.get_queryset()
            serializer = SubscriberSerializer(subscribers, many=True)
            return Response(serializer.data)
        subscribers = Subscriber.objects.filter(reseller=user)
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data)


class SubscriberDetailView(generics.RetrieveAPIView):
    """Detail of subscriber"""
    queryset = Subscriber.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriberDetailSerializer


class SubscriberEditView(generics.UpdateAPIView):
    queryset = Subscriber.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = SubscriberCreateSerializer


class SubscriberCreateView(generics.CreateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = SubscriberCreateSerializer
    queryset = Subscriber.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.user
        subscriber = Subscriber.objects.create(
            reseller=user,
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            email=request.data.get('email'),
            address=request.data.get('address'),
            telephone=request.data.get('telephone')
        )
        log = 'DATE: {}; ID SUBSCRIBER: {}; LOG: Created;'
        logging(LogsSubscriber, subscriber, log)
        serializer = SubscriberDetailSerializer(subscriber)
        return Response(serializer.data, status=HTTP_201_CREATED)


class SubscriberDeleteView(generics.DestroyAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = SubscriberDetailSerializer
    queryset = Subscriber.objects.all()

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        subscriber = Subscriber.objects.get(pk=pk)
        subscriber.cards.clear()
        subscriber.delete()
        log = 'DATE: {}; ID SUBSCRIBER: {}; LOG: Deleted;'
        logging(LogsSubscriber, subscriber, log)
        return Response(data={'message': 'Deleted'},
                        status=HTTP_200_OK)


class SubscriberUpdateCardsView(APIView):
    permission_classes = [IsOwner, IsAuthenticated]

    def get(self, request, pk):
        user = request.user
        cards = user.cards.filter(subscriber=None)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        settings = Settings.objects.first()
        subscriber = Subscriber.objects.get(pk=kwargs['pk'])
        subscriberCards = subscriber.cards.all()
        data = list(subscriberCards)
        card_pk = request.data.get('card')
        card = Card.objects.get(pk=card_pk)
        reseller = subscriber.reseller

        if card in subscriberCards:
            return Response({'detail': 'This card already exists'},
                            status=HTTP_400_BAD_REQUEST)

        if settings.kind_payment == 'VIRTUAL':

            if subscriber.balance - card.price() < 0:
                return Response({'detail': 'Cannot add card.'},
                                status=HTTP_400_BAD_REQUEST)

            period = int(settings.quantity)

            if settings.kind_period == 'MONTHS':
                card.expired_date = datetime.now() + relativedelta(months=period)
            elif settings.kind_period == 'WEEKS':
                card.expired_date = datetime.now() + relativedelta(weeks=period)
            elif settings.kind_period == 'DAYS':
                card.expired_date = datetime.now() + relativedelta(minutes=period)

            card.save(update_fields=['expired_date'])
            log = 'DATE: {}; ID CARD: {}; LOG: Update expired date - {};'
            logging(LogsCard, card, log, card.expired_date)
            subscriber.balance -= card.price()
            log = 'DATE: {}; ID SUBSCRIBER: {}; LOG: Payed. Balance - {}, Price - {};'
            logging(LogsSubscriber, subscriber, log, subscriber.balance, card.price())

        data.append(card)
        subscriber.cards.set(data)
        subscriber.save()
        log = 'DATE: {}; ID CARD: {}; LOG: Reseller ({}, {}, {}) handed subscriber ({}, {}, {}) the card;'
        logging(LogsCard, card, log, reseller.id, reseller.username, reseller.email,
                subscriber.id, subscriber.first_name, subscriber.last_name)
        log = 'DATE: {}; ID SUBSCRIBER: {}; LOG: Get card (id - {});'
        logging(LogsSubscriber, subscriber, log, card.id)
        serializer = SubscriberEditCardsSerializer(subscriber)
        return Response(serializer.data)


class SubscriberDeleteCardView(APIView):
    permission_classes = [IsOwner, IsAuthenticated]

    def put(self, request, **kwargs):
        pk = kwargs['pk']
        subscriber = Subscriber.objects.get(pk=pk)
        subscriberCards = subscriber.cards.all()
        data = list(subscriberCards)
        user = request.user
        card_pk = request.data.get('card')
        querysetcard = user.cards.filter(pk=int(card_pk))
        if querysetcard.first() is None:
            raise generics.ValidationError('This card is not your')
        data.remove(querysetcard.first())
        subscriber.cards.set(data)
        subscriber.save()
        reseller = subscriber.reseller
        log = 'DATE: {}; ID CARD: {}; LOG: Reseller ({}, {}, {}) pick up the card from subscriber ({}, {}, {});'
        logging(LogsCard, querysetcard.first(), log, reseller.id, reseller.username, reseller.email,
                subscriber.id, subscriber.first_name, subscriber.last_name)
        serializer = SubscriberEditCardsSerializer(subscriber)
        return Response(serializer.data)


class SubscriberUpdateBalanceView(generics.UpdateAPIView):
    queryset = Subscriber.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = SubscriberEditBalanceSerializer

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        subscriber = Subscriber.objects.get(pk=pk)
        new_balance = int(request.data['balance'])
        user = request.user
        diff = user.balance - new_balance
        if diff > 0:
            subscriber.balance += new_balance
            user.balance -= new_balance
        else:
            if user.credit > diff:
                return Response({'detail': 'Your balance cannot be less your credit'},
                                status=HTTP_400_BAD_REQUEST)
            else:
                subscriber.balance += new_balance
                user.balance -= new_balance
        user.save(update_fields=['balance'])
        subscriber.save(update_fields=['balance'])
        log = 'DATE: {}; ID SUBSCRIBER: {}; LOG: Edit balance. New value - {};'
        logging(LogsSubscriber, subscriber, log, subscriber.balance)
        serializer = self.get_serializer(instance=subscriber)
        return Response(serializer.data)


class ResetPasswordRequestView(APIView):
    """Form for email for request"""
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = PasswordRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data['email']
        user = User.objects.get(email=email)
        reset_password.send(
            sender=ResetPasswordRequestView, instance=user)
        return Response(serializer.data)


class ResetPasswordView(APIView):
    """Update password"""
    permission_classes = [AllowAny]
    authentication_classes = []

    def put(self, request, **kwargs):
        try:
            email = signer.unsign(kwargs['sign'])
        except BadSignature:
            return Response({'errors': 'Badsignature'})
        user = User.objects.get(email=email)
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data['password2'])
        user.save()
        return Response(serializer.data)


class DownloadBouquets(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        count = kwargs['count']
        command = Command()
        command.handle(count=count)
        return Response({'bouquets': f'saved {count} bouquets'})


class BouquetsFilterListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BouquetShortDescriptionSerializer
    queryset = Bouquet.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        package = Packet.objects.get(pk=pk)
        bouquets = Bouquet.objects.all().difference(package.bouquets.all())
        serializer = self.get_serializer(bouquets, many=True)
        return Response(serializer.data)


class PackageUpdateBouquetsView(generics.UpdateAPIView):
    queryset = Packet.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PackageDetailSerializer

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        package = Packet.objects.get(pk=pk)
        bouquet = Bouquet.objects.get(number=request.data['bouquet'])
        package.bouquets.add(bouquet)
        package.save()
        serializer = self.get_serializer(instance=package)
        return Response(serializer.data)


class PackageRemoveBouquetsView(generics.UpdateAPIView):
    queryset = Packet.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PackageDetailSerializer

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        package = Packet.objects.get(pk=pk)
        bouquet = Bouquet.objects.get(number=request.data['bouquet'])
        package.bouquets.remove(bouquet)
        package.save()
        serializer = self.get_serializer(instance=package)
        return Response(serializer.data)


class SettingsView(generics.RetrieveAPIView):
    queryset = Settings.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = SettingsSerializer

    def get(self, request, *args, **kwargs):
        settings = Settings.objects.first()
        serializer = self.get_serializer(instance=settings)
        return Response(serializer.data)


class ChangeSettingsView(generics.UpdateAPIView):
    queryset = Settings.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SettingsSerializer

    def put(self, request, *args, **kwargs):
        settings = Settings.objects.first()
        print(request.data)
        settings.kind_payment = request.data.get('kind_payment')
        settings.quantity = request.data.get('quantity')
        settings.kind_period = request.data.get('kind_period')
        settings.save()
        serializer = self.get_serializer(instance=settings)
        return Response(serializer.data)


class EnableSuspendSubscriptionView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardSuspendSubscribtionSerializer

    def put(self, request, *args, **kwargs):
        card = Card.objects.get(pk=kwargs['pk'])
        if not card.suspend:
            card.suspend_date = datetime.now()
            card.suspend = True
            card.save(update_fields=['suspend', 'suspend_date'])
            reseller = card.reseller
            log = 'DATE: {}; ID CARD: {}; LOG: Reseller ({}, {}, {}) enable suspend subscription;'
            logging(LogsCard, card, log, reseller.id, reseller.username, reseller.email)
            serializer = self.get_serializer(instance=card)
            return Response(serializer.data)
        return Response(self.get_serializer(instance=card).data)


class DisableSuspendSubscriptionView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardSuspendSubscribtionSerializer

    def put(self, request, *args, **kwargs):
        card = Card.objects.get(pk=kwargs['pk'])
        if card.suspend:
            card.expired_date = datetime.now() + card.suspend_interval()
            card.suspend = False
            card.save(update_fields=['suspend', 'expired_date'])
            reseller = card.reseller
            log = 'DATE: {}; ID CARD: {}; LOG: Reseller ({}, {}, {}) disable suspend subscription;'
            logging(LogsCard, card, log, reseller.id, reseller.username, reseller.email)
            serializer = self.get_serializer(instance=card)
            return Response(serializer.data)
        return Response(self.get_serializer(instance=card).data)


class TieCardsToResellerView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ResellerDetailSerializer

    def put(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        start = int(request.data.get('start'))
        stop = int(request.data.get('stop'))
        tied_cards = []
        for i in range(start, stop + 1):
            try:
                card = Card.objects.get(pk=i)
            except Card.DoesNotExist:
                return Response({'errors': 'Invalid start or stop'})
            tied_cards.append(card)
            log = 'DATE: {}; ID CARD: {}; LOG: Tie card to reseller ({}, {}, {})'
            logging(LogsCard, card, log, user.id, user.username, user.email)
        user.cards.set(tied_cards)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class PickUpCardsFromReseller(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ResellerDetailSerializer

    def put(self, request, *args, **kwargs):
        pk = request.data.get('pk')
        user = User.objects.get(pk=kwargs['pk'])
        card = Card.objects.get(reseller=user, pk=pk)
        if not user.is_superuser:
            card.reseller = User.objects.get(is_superuser=True)
        card.save()
        log = 'DATE: {}; ID CARD: {}; LOG: Pick up card from reseller ({}, {}, {})'
        logging(LogsCard, card, log, user.id, user.username, user.email)
        serializer = self.get_serializer(instance=user)
        return Response(serializer.data)


# class GetLogsCardView(generics.ListAPIView):
#     queryset = LogsCard.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = LogsCardSerializer
#
#     def get(self, request, *args, **kwargs):
#         card = Card.objects.get(pk=kwargs['pk'])
#         log = card.logs
#         serializer = self.get_serializer(log, many=True)
#         return Response(serializer.data)
