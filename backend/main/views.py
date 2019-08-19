from datetime import datetime
from dateutil.relativedelta import relativedelta
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
    reset_password,
)
from .serializer import (
    ResellerCreateSerializer,
    ResellerSerializer,
    PackageListSerializer,
    PackageDetailSerializer,
    PackageCreateSerializer,
    PackageDeleteSerializer,
    PackageEditSerializer,
    CardSerializer,
    CardCreateSerializer,
    CardDetailSerializer,
    CardUpdateStatusSerializer,
    CardUpdateExpiredSerializer,
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
            if user.check_password(password):
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
            serializer = ResellerSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)


class ResellerListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ResellerSerializer
    queryset = User.objects.all()


class ResellerDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ResellerSerializer


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
        pk = kwargs['pk']
        card = Card.objects.get(pk=pk)
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


class CardListView(APIView):
    """Show list of Cards for owner"""
    permission_classes = [IsOwner, IsAuthenticated]

    def get(self, request):
        user = request.user
        cards = Card.objects.filter(reseller=user)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


class CardCreateView(generics.CreateAPIView):
    """Create a Card"""
    permission_classes = [IsAdminUser]
    serializer_class = CardCreateSerializer
    queryset = Card.objects.all()


class CardDetailView(generics.RetrieveAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardDetailSerializer
    queryset = Card.objects.all()


class CardUpdateExpiredView(generics.UpdateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardUpdateExpiredSerializer
    queryset = Card.objects.all()

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        period = int(request.data.get('period'))
        if period == 0:
            return Response({'detail': 'Period cannot equal to 0'},
                            status=HTTP_400_BAD_REQUEST)
        settings = Settings.objects.first()
        card = Card.objects.get(pk=pk)
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
        serializer = self.get_serializer(instance=card)
        return Response(serializer.data)


class CardUpdateStatusView(generics.UpdateAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CardUpdateStatusSerializer
    queryset = Card.objects.all()


class CardUpdatePackageView(APIView):
    permission_classes = [IsOwner, IsAuthenticated]

    def put(self, request, **kwargs):
        pk = kwargs['pk']
        card = Card.objects.get(pk=pk)
        # if card.expired_date is None:
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
        serializer = CardSerializer(card)
        return Response(serializer.data)
        # return Response({'detail': 'You can add packages when card will be expired'},
        #                 status=HTTP_400_BAD_REQUEST)


class CardRemovePackageView(APIView):
    permission_classes = [IsOwner, IsAuthenticated]

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
        serializer = CardSerializer(card)
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
        pk = kwargs['pk']
        settings = Settings.objects.first()
        subscriber = Subscriber.objects.get(pk=pk)
        subscriberCards = subscriber.cards.all()
        data = list(subscriberCards)
        card_pk = request.data.get('card')
        card = Card.objects.get(pk=card_pk)
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
            subscriber.balance -= card.price()
        data.append(card)
        subscriber.cards.set(data)
        subscriber.save()
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
