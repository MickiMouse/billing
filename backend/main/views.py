from django.shortcuts import get_object_or_404
from django.core.signing import BadSignature
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Subscriber, Reseller
from .permission import IsOwnerOrReadOnly
from .serializer import (
    SubscriberSerializer,
    CardSerializer,
    ResellerCreateSerializer,
    ResellerSerializer,
)
from .utilities import signer

User = get_user_model()


class SubscriberView(APIView):
    """Data of subscriber"""
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        subscribers = request.user.subscriber_set.all()
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data)


class CardsView(APIView):
    """Cards of subscriber"""
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk):
        sub = Subscriber.objects.get(pk=pk)
        cards = sub.card_set.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


class ResellerRegisterAPIView(generics.CreateAPIView):
    serializer_class = ResellerCreateSerializer
    queryset = User.objects.all()


class ResellerActivateAPIView(generics.GenericAPIView):
    """Confirm user"""

    def get(self, request, sign):
        try:
            username = signer.unsign(sign)
        except BadSignature:
            return Response({'errors': 'Badsignature'})
        user = get_object_or_404(Reseller, username=username)
        if user.is_activated:
            return Response({'message': 'User is activated'})
        else:
            user.is_active = True
            user.is_activated = True
            user.save()
            serializer = ResellerSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)
