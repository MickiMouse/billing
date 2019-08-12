from django.shortcuts import get_object_or_404
from django.core.signing import BadSignature
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_404_NOT_FOUND)
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
    Card,
    Subscriber,
    reset_password,
)
from .serializer import (
    TokenSerializer,
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
    SubscriberSerializer,
    SubscriberDetailSerializer,
    SubscriberEditCardsSerializer,
    SubscriberEditBalanceSerializer,
    SubscriberCreateSerializer,
    PasswordRequestSerializer,
    PasswordSerializer,
)
from .utilities import signer

User = get_user_model()


class TokenDestroyView(APIView):
    """Logout"""
    permission_classes = [IsAuthenticated]
    serializer_class = TokenSerializer

    def post(self, request):
        user = request.user
        t = Token.objects.get(user=user)
        t.delete()
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
            return Response({'message': 'User is activated'})
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
    permission_classes = [IsAdminUser, IsAuthenticated]
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


class CardDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class CardUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class CardUpdatePackageView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, **kwargs):
        pk = kwargs['pk']
        card = Card.objects.get(pk=pk)
        cardPackages = card.packages.all()
        data = list(cardPackages)
        package_pk = request.data.get('package')
        package = Packet.objects.filter(pk=int(package_pk))
        if package.first() is None:
            raise generics.ValidationError('Cannot add this package')
        data.append(package.first())
        card.packages.set(data)
        card.save()
        serializer = CardSerializer(card)
        return Response(serializer.data)


class CardRemovePackageView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, **kwargs):
        pk = kwargs['pk']
        card = Card.objects.get(pk=pk)
        cardPackages = card.packages.all()
        data = list(cardPackages)
        package_pk = request.data.get('package')
        package = Packet.objects.filter(pk=int(package_pk))
        if package.first() is None:
            raise generics.ValidationError('Cannot remove this package')
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
        # if user.is_superuser:
        #     subscribers = self.get_queryset()
        #     serializer = SubscriberSerializer(subscribers, many=True)
        #     return Response(serializer.data)
        subscribers = Subscriber.objects.filter(reseller=user)
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data)


class SubscriberDetailView(generics.RetrieveAPIView):
    """Detail of subscriber"""
    queryset = Subscriber.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = SubscriberDetailSerializer

    # def get(self, request, pk):
    #     subscriber = Subscriber.objects.get(pk=pk)
    #     serializer = SubscriberDetailSerializer(subscriber)
    #     return Response(serializer.data)


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

    def get(self, request):
        user = request.user
        cards = user.cards.filter(subscriber=None)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        pk = kwargs['pk']
        subscriber = Subscriber.objects.get(pk=pk)
        subscriberCards = subscriber.cards.all()
        card_pk = request.data.get('card')
        card = Card.objects.filter(pk=card_pk)
        if subscriberCards.intersection(card).exists():
            return Response({'detail': 'This card already exists'})
        user = request.user
        data = list(subscriberCards)
        querysetcard = user.cards.filter(pk=card_pk)
        if not querysetcard.exists():
            return Response({'detail': 'Unable to find such a card'},
                            status=HTTP_404_NOT_FOUND)
        for i in range(len(querysetcard)):
            data.append(querysetcard[i])
        subscriber.cards.set(data)
        subscriber.balance -= querysetcard.first().price()
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
        new_balance = request.data['balance']
        user = request.user
        diff = user.balance - new_balance
        if diff > 0:
            subscriber.balance += new_balance
            user.balance -= new_balance
        else:
            if user.credit > diff:
                raise generics.ValidationError(
                    'Your balance cannot be less your credit')
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

    def get(self, request, **kwargs):
        return Response(kwargs)

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
