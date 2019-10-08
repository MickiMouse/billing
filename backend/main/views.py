from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from django.core.signing import BadSignature
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_204_NO_CONTENT,
                                   HTTP_401_UNAUTHORIZED)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.decorators import api_view
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
    DelayedAdditionPackage,
    DelayedRemovePackage,
    ReportSubscription,
    SynchronizeForms,
    ReportFinance,
    reset_password,
)
from .serializer import (
    ResellerCreateSerializer,
    ResellerListSerializer,
    ResellerDetailSerializer,
    ResellerUpdateSerializer,
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
    CardShortDescriptionSerializer,
    SubscriberSerializer,
    SubscriberDetailSerializer,
    SubscriberEditCardsSerializer,
    SubscriberEditBalanceSerializer,
    SubscriberCreateSerializer,
    PasswordRequestSerializer,
    PasswordSerializer,
    BouquetShortDescriptionSerializer,
    SettingsSerializer,
    DelayedPackageSerializer,
    ResellerTieOneCardSerializer,
    ResellerMakeAdminSerializer,
    SynchrFormsSerializer,
    LogsSubscriberSerializer,
    DestroyCard,
    ResellerUpdateBalanceSerializer,
    ResellerConfirmSerializer,
    ResellersTableSerializer,
)

from .api import (
    Command,
    SendCards,)


def logging(class_, instance, text, *args):
    try:
        getattr(class_, 'card')
        log = class_.objects.create(card=instance)
        log.log = text.format(instance.id, *args)
        log.save()
    except AttributeError:
        pass

    try:
        getattr(class_, 'subscriber')
        log = class_.objects.create(subscriber=instance)
        log.log = text.format(instance.id, *args)
        log.save()
    except AttributeError:
        pass

    try:
        getattr(class_, 'reseller')
        log = class_.objects.create(reseller=instance)
        log.log = text.format(instance.id, *args)
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
        if not user.is_confirm:
            return Response(status=HTTP_401_UNAUTHORIZED)
        token = Token.objects.filter(user=user)
        settings = Settings.objects.first()
        if token.exists():
            return Response({'auth_token': token.first().key, 'is_superuser': user.is_superuser,
                             'currency': settings.currency})
        else:
            if user.check_password(password) and user.is_activated:
                token = Token.objects.create(user=user)
                return Response({'auth_token': token.key, 'is_superuser': user.is_superuser,
                                 'currency': settings.currency})
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
            user.is_confirm = False
            user.save()
            log = 'ID RESELLER: {}; LOG: Registered;'
            logging(LogsReseller, user, log)
            serializer = ResellerDetailSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)


from .utilities import signer


class ResellerListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ResellerListSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_confirm=True)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


class ResellerConfirmView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ResellerConfirmSerializer
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        user.is_confirm = True
        user.save()
        return Response(status=HTTP_200_OK)


class ResellersUnconfirmed(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ResellersTableSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_confirm=False)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


class ResellerDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ResellerDetailSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])

        if request.user.is_superuser:
            admin = request.user
            cards = Card.objects.filter(reseller=admin)
        else:
            cards = []

        result = {}
        serializer = self.get_serializer(user)
        serializer_cards = CardShortDescriptionSerializer(cards, many=True)
        result.update(serializer.data)
        result.update({'available_cards': serializer_cards.data})
        return Response(result)


class ResellerEditView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ResellerUpdateSerializer


class ResellerEditBalanceView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ResellerUpdateBalanceSerializer


class ResellerDeleteView(generics.DestroyAPIView):
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
        delayed = DelayedAdditionPackage.objects.filter(card_id=kwargs['pk'])
        for i in range(len(serializer.data)):
            pk = serializer.data[i].get('pk')
            for d in delayed:
                if pk == d.package_id:
                    serializer.data[i].update({'delayed': True})
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

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            cards = Card.objects.all()
            serializer = self.get_serializer(cards, many=True)
            return Response(serializer.data)
        cards = request.user.cards.all()
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data)


class CardCreateView(generics.CreateAPIView):
    """Create a Card"""
    permission_classes = [IsAdminUser]
    serializer_class = CardCreateSerializer
    queryset = Card.objects.all()

    def create(self, request, *args, **kwargs):
        pk = Card.objects.aggregate(maxpk=models.Max('pk'))['maxpk']
        card, created = Card.objects.get_or_create(pk=pk+1, reseller=request.user)
        print(card, created)
        if created:
            log = 'ID CARD: {}; LOG: Created card;'
            logging(LogsCard, card, log)
            logging(LogsReseller, request.user, log)
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data, status=HTTP_201_CREATED)


class CreateRangeCardView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CardCreateSerializer

    def get(self, request, *args, **kwargs):
        max_pk = Card.objects.aggregate(max_pk=models.Max('pk'))['max_pk']
        return Response({'start': max_pk + 1})

    def create(self, request, *args, **kwargs):
        start = request.data.get('start')
        stop = request.data.get('stop')
        print(request.data)
        created_cards = []
        for i in range(start, stop + 1):
            card, created = Card.objects.get_or_create(pk=i, reseller=request.user)
            if created:
                created_cards.append(card)
                log = 'ID CARD: {}; LOG: Created card;'
                logging(LogsCard, card, log)
                logging(LogsReseller, request.user, log)
        serializer = self.get_serializer(created_cards, many=True)
        return Response(serializer.data, status=HTTP_201_CREATED)


class CardDetailView(generics.RetrieveAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardDetailSerializer
    queryset = Card.objects.all()

    def get(self, request, *args, **kwargs):
        card = Card.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(card)
        delayed = DelayedRemovePackage.objects.filter(card_id=kwargs['pk'])
        packages = serializer.data.get('packages')
        for package in packages:
            for d in delayed:
                if package.get('pk') == d.package_id:
                    package.update({'delayed': True})
        return Response(serializer.data)


class CardUpdateExpiredView(generics.UpdateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardUpdateExpiredSerializer
    queryset = Card.objects.all()

    def put(self, request, *args, **kwargs):
        settings = Settings.objects.first()
        if settings.kind_payment == 'PREPAYMENT':
            period = int(request.data.get('period'))
            if period <= 0:
                return Response({'detail': 'Period cannot equal to 0 or less 0'},
                                status=HTTP_400_BAD_REQUEST)
            card = Card.objects.get(pk=kwargs['pk'])
            if card.status() == 'Inactive' or card.status() == 'Suspend':
                return Response({'errors': 'Cannot update expired date'})
            quantity = settings.quantity
            total_period = period * quantity
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
        log = 'ID CARD: {}; LOG: Update expired date {};'
        logging(LogsCard, card, log, card.expired_date)
        logging(LogsReseller, request.user, log, card.expired_date)
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data)


class CardDelayedUpdatePackageView(generics.CreateAPIView):
    queryset = DelayedAdditionPackage.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DelayedPackageSerializer

    def post(self, request, *args, **kwargs):
        card_pk = kwargs['pk']
        package_pk = request.data.get('package')
        if not Card.objects.get(pk=card_pk).packages.filter(pk=package_pk).exists():
            delayed, created = DelayedAdditionPackage.objects.get_or_create(
                card_id=card_pk,
                package_id=package_pk)
            serializer = self.get_serializer(delayed)
            return Response(serializer.data)
        return Response({'detail': 'Cannot add package'})


class CardDelayedRemovePackageView(generics.CreateAPIView):
    queryset = DelayedRemovePackage.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DelayedPackageSerializer

    def post(self, request, *args, **kwargs):
        card_pk = kwargs['pk']
        package_pk = request.data.get('package')
        if Card.objects.get(pk=card_pk).packages.filter(pk=package_pk).exists():
            delayed, created = DelayedRemovePackage.objects.get_or_create(
                card_id=card_pk,
                package_id=package_pk)
            serializer = self.get_serializer(delayed)
            return Response(serializer.data)
        return Response({'detail': 'Cannot delete package'})


class CardForceUpdatePackageView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardSerializer

    def put(self, request, *args, **kwargs):
        settings = Settings.objects.first()
        card = Card.objects.get(pk=kwargs['pk'])
        cardPackages = card.packages.all()
        data = list(cardPackages)
        package_pk = request.data.get('package')
        package = Packet.objects.get(pk=package_pk)

        q = DelayedAdditionPackage.objects.filter(package_id=package_pk)
        if q.exists():
            q.delete()

        data.append(package)

        if card.subscriber:
            if settings.kind_payment == 'VIRTUAL':
                subscriber = card.subscriber

                if subscriber.balance - package.tariff >= 0:
                    subscriber.balance -= package.tariff
                    subscriber.save()
                    card.packages.set(data)
                    card.save()
                else:
                    return Response({'errors': 'Not enough money in the account'},
                                    status=HTTP_400_BAD_REQUEST)
            else:
                card.packages.set(data)
                card.save()

        log = 'ID CARD: {}; LOG: Add package {};'
        logging(LogsCard, card, log, package.header)
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data)


class CardForceRemovePackageView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardSerializer

    def put(self, request, **kwargs):
        card = Card.objects.get(pk=kwargs['pk'])
        cardPackages = card.packages.all()
        data = list(cardPackages)
        package_pk = request.data.get('package')
        package = Packet.objects.get(pk=package_pk)
        if card.subscriber:
            subscriber = card.subscriber
            subscriber.balance += package.tariff
            subscriber.save()
        data.remove(package)
        card.packages.set(data)
        card.save()
        q = DelayedRemovePackage.objects.filter(package_id=package_pk)
        if q.exists():
            q.delete()
        log = 'ID CARD: {}; LOG: Remove package {};'
        logging(LogsCard, card, log, package.header)
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data)


class CardDeleteView(generics.DestroyAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = DestroyCard

    def destroy(self, request, *args, **kwargs):
        pk = kwargs['pk']
        card = Card.objects.get(pk=pk)
        if card.status() == 'Active' or card.subscriber is not None:
            return Response({'errors': 'Cannot delete this card'},
                            status=HTTP_400_BAD_REQUEST)
        if card.delete_date() > datetime.now():
            log = 'ID CARD: {}; LOG: Remove card;'
            logging(LogsCard, card, log)
            logging(LogsReseller, request.user, log)
            card.logs.clear()
            card.delete()
            serializer = self.get_serializer(instance=card)
            return Response(serializer.data, status=HTTP_204_NO_CONTENT)
        return Response({'errors': '3 days have passed'},
                        status=HTTP_400_BAD_REQUEST)


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
    permission_classes = [IsOwner]
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
        log = 'ID SUBSCRIBER: {}; LOG: Created;'
        logging(LogsSubscriber, subscriber, log)
        logging(LogsReseller, user, log)
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
        log = 'ID SUBSCRIBER: {}; LOG: Deleted;'
        logging(LogsSubscriber, subscriber, log)
        logging(LogsReseller, request.user, log)
        subscriber.logs.clear()
        subscriber.delete()
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
                card.expired_date = datetime.now() + relativedelta(days=period)
            card.save(update_fields=['expired_date'])
            log = 'ID CARD: {}; LOG: Update expired date - {};'
            logging(LogsCard, card, log, card.expired_date)
            subscriber.balance -= card.price()
            log = 'ID SUBSCRIBER: {}; LOG: Payed. Price - {}; Balance - {};'
            logging(LogsSubscriber, subscriber, log, subscriber.balance, card.price())
            log = 'Card add to subscriber'
            logging(LogsReseller, request.user, log)

        data.append(card)
        subscriber.cards.set(data)
        subscriber.save()
        count = 0
        for s in reseller.subscriber_set.all():
            count += s.cards.count()
        ReportSubscription.objects.create(reseller=reseller, subscription=count)
        log = 'ID CARD: {}; LOG: Reseller ({}, {}, {}) handed subscriber ({}, {}, {}) the card;'
        logging(LogsCard, card, log, reseller.id, reseller.username, reseller.email,
                subscriber.id, subscriber.first_name, subscriber.last_name)
        log = 'ID SUBSCRIBER: {}; LOG: Get card (id - {});'
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
        log = 'ID CARD: {}; LOG: Reseller ({}, {}, {}) pick up the card from subscriber ({}, {}, {});'
        logging(LogsCard, querysetcard.first(), log, reseller.id, reseller.username, reseller.email,
                subscriber.id, subscriber.first_name, subscriber.last_name)
        logging(LogsReseller, request.user, log, reseller.id, reseller.username, reseller.email,
                subscriber.id, subscriber.first_name, subscriber.last_name)
        serializer = SubscriberEditCardsSerializer(subscriber)
        return Response(serializer.data)


class SubscriberUpdateBalanceView(generics.UpdateAPIView):
    queryset = Subscriber.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = SubscriberEditBalanceSerializer

    def put(self, request, *args, **kwargs):
        subscriber = Subscriber.objects.get(pk=kwargs['pk'])
        new_balance = request.data['balance']
        user = request.user

        difference = new_balance - subscriber.balance

        if difference >= 0:
            user.balance -= difference
            ReportFinance.objects.create(spend_money=new_balance,
                                         reseller=user)
        else:
            user.balance += difference

        subscriber.balance = new_balance
        user.save(update_fields=['balance'])
        subscriber.save(update_fields=['balance'])
        log = 'ID SUBSCRIBER: {}; LOG: Edit balance. New value - {};'
        logging(LogsSubscriber, subscriber, log, subscriber.balance)
        logging(LogsReseller, user, log, subscriber.balance)
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
        result = {}
        serializer = self.get_serializer(instance=settings)
        result.update(serializer.data)
        array_times = []
        for time in SynchronizeForms.objects.all():
            array_times.append({'value': time.date.strftime('%H:%M')})
        length = 8 - len(array_times)
        for i in range(length):
            array_times.append({})
        result.update({'periods': array_times})
        return Response(result)


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
        settings.sssss = request.data.get('sssss')
        settings.max_cards = request.data.get('max_cards')
        settings.server_port = request.data.get('server_port')
        settings.server_ip = request.data.get('server_ip')
        settings.currency = request.data.get('currency')
        settings.save()
        serializer = self.get_serializer(instance=settings)
        return Response(serializer.data)


class SuspendSubscriptionView(generics.UpdateAPIView):
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
            log = 'ID CARD: {}; LOG: Reseller ({}, {}, {}) enable suspend subscription;'
            logging(LogsCard, card, log, reseller.id, reseller.username, reseller.email)
            serializer = self.get_serializer(instance=card)
            return Response(serializer.data)
        else:
            card.expired_date = datetime.now() + card.suspend_interval()
            card.suspend = False
            card.save(update_fields=['suspend', 'expired_date'])
            reseller = card.reseller
            log = 'ID CARD: {}; LOG: Reseller ({}, {}, {}) disable suspend subscription;'
            logging(LogsCard, card, log, reseller.id, reseller.username, reseller.email)
            serializer = self.get_serializer(instance=card)
            return Response(serializer.data)


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
            log = 'ID CARD: {}; LOG: Reseller ({}, {}, {}) disable suspend subscription;'
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
                return Response({'errors': 'Invalid start or stop'},
                                status=HTTP_400_BAD_REQUEST)
            tied_cards.append(card)
            log = 'ID CARD: {}; LOG: Tie card to reseller ({}, {}, {})'
            logging(LogsCard, card, log, user.id, user.username, user.email)
            logging(LogsReseller, user, log, user.id, user.username, user.email)
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
        log = 'ID CARD: {}; Pick up card from reseller ({}, {}, {})'
        logging(LogsCard, card, log, user.id, user.username, user.email)
        logging(LogsReseller, user, log, user.id, user.username, user.email)
        serializer = self.get_serializer(instance=user)
        return Response(serializer.data)


class ResellerFilterCards(generics.ListAPIView):
    queryset = Card.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CardShortDescriptionSerializer

    def get(self, request, *args, **kwargs):
        cards = Card.objects.filter(reseller__is_superuser=True)
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data)


class ResellerTieOneCard(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ResellerTieOneCardSerializer

    def put(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        card = Card.objects.get(pk=request.data.get('card'))
        cards = list(user.cards.all())
        cards.append(card)
        user.cards.set(cards)
        user.save()
        serializer = self.get_serializer(user)
        log = 'ID CARD: {}; Tie card to reseller ({}, {}, {})'
        logging(LogsReseller, user, log, user.id, user.username, user.email)
        return Response(serializer.data)


class ResellerPickUpOneCard(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ResellerTieOneCardSerializer

    def put(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        card = Card.objects.get(pk=request.data.get('card'))
        card.reseller = request.user
        card.save(update_fields=['reseller'])
        serializer = self.get_serializer(user)
        log = 'ID CARD: {}; Pick up card from reseller ({}, {}, {})'
        logging(LogsReseller, user, log, user.id, user.username, user.email)
        return Response(serializer.data)


class SendCardsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        start = request.data.get('start')
        stop = request.data.get('stop')
        command = SendCards()
        command.handle(start=start, stop=stop)
        return Response({'start': start,
                         'stop': stop})


class MakeAdmin(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ResellerMakeAdminSerializer


class ChangeSelfPermission(APIView):

    def get(self, request, **kwargs):
        user_one = request.user
        user_two = User.objects.get(pk=kwargs['pk'])
        res = {}
        if user_one.pk == user_two.pk:
            res.update({'permission': False})
        else:
            res.update({'permission': True})
        return Response(res)


class SynchronizeView(APIView):

    def post(self, request):
        periods = request.data.get('periods')
        date = str(datetime.now().date()).split('-')
        date = [int(n) for n in date]
        for sync in SynchronizeForms.objects.all():
            sync.delete()
        for val in periods:
            if val is not None and 'value' in val:
                time = val['value'].split(':')
                time = [int(n) for n in time]
                result = datetime.time(datetime(*date, *time))
                SynchronizeForms.objects.create(date=result)
        objs = SynchronizeForms.objects.all()
        serializer = SynchrFormsSerializer(objs, many=True)
        return Response(serializer.data)


class Dashboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dates = []
        cards_count = []
        subscribers_count = []
        dates_dict = Subscriber.objects.values('created_at__day',
                                               'created_at__month',
                                               'created_at__year').distinct()

        for date in dates_dict:
            d = datetime(date['created_at__year'], date['created_at__month'], date['created_at__day'] + 1)
            if d not in dates:
                dates.append(d)

        for date in dates:
            cards = Subscriber.objects.filter(
                Q(created_at__lt=date)).aggregate(Count('cards'))['cards__count']
            cards_count.append(cards)

            subscribers = Subscriber.objects.filter(
                Q(created_at__lt=date)).count()
            subscribers_count.append(subscribers)

        dates = ['T'.join(str(date).split()) for date in dates]

        result = {'x': dates, 'cards': cards_count,
                  'subs': subscribers_count}
        return Response(result)


class ReportSubsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        """

        :param request:
        :return: Count subscribers by reseller
        """
        print(request.data)
        datelt = request.data.get('dateLt', None)
        datert = request.data.get('dateRt', None)
        if datelt and datert:
            q = Q(subscriber__created_at__gt=datelt) & Q(subscriber__created_at__lt=datert)
        else:
            q = None
        result = {}
        objects = []
        totalSubs = Subscriber.objects.count()
        for user in User.objects.annotate(subs=Count('subscriber', filter=q if q else Q())):
            objects.append({'name': user.username, 'item': user.subs})
        result['objects'] = objects
        result['total'] = totalSubs
        return Response(result)


class ReportCardsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        """

        :param request:
        :return: Count cards tied to subscribers
        """
        print(request.data)
        datelt = request.data.get('dateLt', None)
        datert = request.data.get('dateRt', None)
        if datelt and datert:
            q = Q(created_at__gt=datelt) & Q(created_at__lt=datert)
            q2 = Q(cards__created_at__gt=datelt) & Q(cards__created_at__lt=datert)
        else:
            q = None
            q2 = None
        result = {}
        objects = []
        totalCards = Card.objects.filter(~Q(subscriber=None) & q if q else Q()).count()
        for user in User.objects.annotate(cs=Count('cards', filter=~Q(cards__subscriber=None) & q2 if q2 else Q())):
            objects.append({'name': user.username, 'item': user.cs})
        result['objects'] = objects
        result['total'] = totalCards
        return Response(result)


class ReportLogsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        """

        :param request:
        :return: Logs of subscriber
        """
        print(request.data)
        datelt = request.data.get('dateLt', None)
        datert = request.data.get('dateRt', None)
        if datelt and datert:
            q = Q(date__lt=datert) & Q(date__gt=datelt)
        else:
            q = None
        email = request.data.get('email')
        subscriber = Subscriber.objects.get(email=email)
        logs = subscriber.logs.filter(Q(subscriber=subscriber) & q if q else Q())
        serializer = LogsSubscriberSerializer(logs, many=True)
        return Response(serializer.data)


class ReportFinanceView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        """

        :param request:
        :return: Spend money reseller
        """
        print(request.data)
        datelt = request.data.get('dateLt', None)
        datert = request.data.get('dateRt', None)
        if datelt and datert:
            q = Q(created_at__lt=datert) & Q(created_at__gt=datelt)
        else:
            q = None
        result = {}
        objects = []
        totalMoney = ReportFinance.objects.filter(q if q else Q()).aggregate(
            money=models.Sum('spend_money'))['money']
        for user in User.objects.all():
            money = user.reports_finance.filter(q if q else Q()).aggregate(money=models.Sum('spend_money'))['money']
            objects.append({'name': user.username, 'item': 0 if money is None else money})
        result['objects'] = objects
        result['total'] = totalMoney
        return Response(result)


class ReportCardsOfResellerView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        """

        :param request:
        :return: Cards of reseller
        """
        result = {}
        objects = []
        totalCards = Card.objects.count()
        for user in User.objects.all():
            cards = [card.pk for card in user.cards.all()]
            cards.sort()
            cards = pks(cards)
            objects.append({'name': user.username,
                            'total': user.cards.count(),
                            'cards': cards})
        result['objects'] = objects
        result['total'] = totalCards
        return Response(result)


def pks(arr):
    through = []
    result = []
    b = None
    if len(arr) == 1:
        result.append(str(arr[0]))
        return result
    for i in range(1, len(arr)):
        a, b = arr[i-1], arr[i]
        if abs(b-a) == 1:
            through.append(a)
        else:
            through.append(a)
            if len(through) == 1:
                result.append(str(a))
                through.clear()
            else:
                result.append(f'{min(through)}...{max(through)}')
                through.clear()
    else:
        through.append(b)
        if len(through) == 1:
            result.append(str(b))
            through.clear()
        else:
            result.append(f'{min(through)}...{max(through)}')
    return result


@api_view(['GET'])
def balance(request):
    if request.method == 'GET':
        return Response({'balance': request.user.balance})


class BalanceUser(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({'balance': request.user.balance})
