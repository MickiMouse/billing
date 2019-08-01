from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Subscriber, Card, user_registrated

User = get_user_model()


class ResellerCreateSerializer(serializers.ModelSerializer):
    """Serializer for Reseller"""
    password2 = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_email(self, value):
        email = value
        if not email:
            raise serializers.ValidationError('Field is required')
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get('password')
        password2 = value
        if password1 != password2:
            raise serializers.ValidationError('Passwords must match')
        return value

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data.pop('password2')
        user_obj = User.objects.create(**validated_data)
        user_obj.set_password(password)
        user_obj.is_active = False
        user_obj.is_activated = False
        user_obj.save()
        user_registrated.send(
            sender=ResellerCreateSerializer, instance=user_obj)
        validated_data['password2'] = password2
        return validated_data


class SubscriberSerializer(serializers.ModelSerializer):
    """Serializer for Subscriber"""

    class Meta:
        model = Subscriber
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    """Serializer for Card"""

    class Meta:
        model = Card
        fields = '__all__'


class ResellerSerializer(serializers.ModelSerializer):
    """Serializer for Reseller"""

    class Meta:
        model = User
        fields = '__all__'
