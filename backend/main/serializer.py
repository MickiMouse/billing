from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .models import (
    Subscriber,
    Card,
    Packet,
    Bouquet,
    Settings,
    LogsCard,
    LogsSubscriber,
    LogsReseller,
    DelayedAdditionPackage,
    SynchronizeForms,
    user_registrated,
)

User = get_user_model()


class ResellerCreateSerializer(serializers.ModelSerializer):
    """Serializer for Register Reseller"""
    password2 = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password',
                  'password2')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_email(self, value):
        email = value
        if not email:
            raise serializers.ValidationError('Field is required')
        user = User.objects.filter(email=email)
        if user:
            raise serializers.ValidationError('Please use different email')
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


class ResellerShortDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email')


class ResellerListSerializer(serializers.ModelSerializer):
    """Serializer for Reseller"""

    class Meta:
        model = User
        fields = ('pk',
                  'rrr',
                  'email',
                  'username',
                  'balance')


class CardSerializer(serializers.ModelSerializer):
    """Serializer for Card"""

    class Meta:
        model = Card
        fields = ('pk',
                  'created_at',
                  'last_change',
                  'expired_date',
                  'status',
                  'label',
                  'price')


class LogsResellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogsReseller
        fields = ('log',
                  'date')


class ResellerDetailSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)
    logs = LogsResellerSerializer(many=True)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'rrr',
                  'address',
                  'telephone',
                  'zone',
                  'balance',
                  'credit',
                  'price_card',
                  'is_activated',
                  'comment',
                  'cards',
                  'logs',
                  'is_superuser')


class ResellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'address',
                  'telephone',
                  'zone',
                  'rrr',
                  'balance',
                  'credit',
                  'price_card',
                  'comment',
                  'is_superuser')


class TokenSerializer(serializers.ModelSerializer):
    """Serializer for Token"""

    class Meta:
        model = Token
        fields = '__all__'


class BouquetSerializer(serializers.ModelSerializer):
    """Serializer for Bouquet"""

    class Meta:
        model = Bouquet
        fields = '__all__'


class BouquetShortDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bouquet
        fields = ('number',
                  'name',
                  'age_limit',)


class PackageListSerializer(serializers.ModelSerializer):
    """Serializer for Packet"""

    class Meta:
        model = Packet
        fields = ('pk',
                  'header',
                  'age_limit',
                  'tariff')


class CardShortDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('pk',
                  'label')


class PackageDetailSerializer(serializers.ModelSerializer):
    """Serializer for detail of package"""
    bouquets = BouquetSerializer(many=True)
    cards = CardShortDescriptionSerializer(many=True)

    class Meta:
        model = Packet
        fields = ('header',
                  'age_limit',
                  'tariff',
                  'cards',
                  'bouquets')


class PackageCreateSerializer(serializers.ModelSerializer):
    """Serializer for adding package"""

    class Meta:
        model = Packet
        fields = ('header',
                  'tariff',)

    def validate(self, attrs):
        header = attrs.get('header')
        tariff = attrs.get('tariff')
        if not header or not tariff:
            raise serializers.ValidationError('Filed is required')
        return attrs


class PackageDeleteSerializer(serializers.ModelSerializer):
    """Delete package"""

    class Meta:
        model = Packet
        fields = '__all__'


class PackageEditSerializer(serializers.ModelSerializer):
    """Edit serializer"""

    class Meta:
        model = Packet
        fields = ('tariff',)


class LogsSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogsSubscriber
        fields = ('log',
                  'date')


class SubscriberSerializer(serializers.ModelSerializer):
    """Serializer for Subscriber"""
    cards = CardShortDescriptionSerializer(many=True)
    reseller = ResellerShortDescriptionSerializer()

    class Meta:
        model = Subscriber
        fields = ('pk',
                  'first_name',
                  'last_name',
                  'email',
                  'balance',
                  'reseller',
                  'cards',)


class CardSuspendSubscribtionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('suspend',
                  'suspend_date',
                  'expired_date')


class CardUpdateExpiredSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('expired_date',)


class SubscriberDetailSerializer(serializers.ModelSerializer):
    """Serializer for detail of subscriber"""
    cards = CardSerializer(many=True)
    reseller = ResellerShortDescriptionSerializer()
    logs = LogsSubscriberSerializer(many=True)

    class Meta:
        model = Subscriber
        fields = ('id',
                  'first_name',
                  'last_name',
                  'address',
                  'telephone',
                  'email',
                  'balance',
                  'reseller',
                  'cards',
                  'logs')


class SubscriberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('first_name',
                  'last_name',
                  'email',
                  'address',
                  'telephone')


class SubscriberEditCardsSerializer(serializers.ModelSerializer):
    cards = serializers.StringRelatedField(many=True)

    class Meta:
        model = Subscriber
        fields = ('cards',)


class SubscriberEditBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('balance',)

    def validate(self, attrs):
        balance = attrs['balance']
        if balance <= 0:
            raise serializers.ValidationError(
                'Balance cannot be less or equal zero'
            )
        return attrs


class CardCreateSerializer(serializers.ModelSerializer):
    """Serializer for adding card"""

    class Meta:
        model = Card
        fields = '__all__'


class LogsCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogsCard
        fields = ('log',
                  'date')


class CardDetailSerializer(serializers.ModelSerializer):
    packages = PackageListSerializer(many=True)
    reseller = ResellerShortDescriptionSerializer()
    subscriber = SubscriberSerializer()
    logs = LogsCardSerializer(many=True)

    class Meta:
        model = Card
        fields = ('pk',
                  'created_at',
                  'last_change',
                  'expired_date',
                  'status',
                  'label',
                  'packages',
                  'price',
                  'reseller',
                  'subscriber',
                  'logs',)


class PasswordRequestSerializer(serializers.ModelSerializer):
    """Form for email"""
    email = serializers.EmailField(label='Email address', required=True)

    class Meta:
        model = User
        fields = ('email',)

    def validate(self, attrs):
        email = attrs.get('email')
        user = User.objects.get(email=email)
        if user:
            return attrs
        else:
            raise serializers.ValidationError('There is no user with such email')


class PasswordSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='Repeat password', min_length=8, required=True)

    class Meta:
        model = User
        fields = ('password',
                  'password2')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if not password or not password2:
            raise serializers.ValidationError('Field is required')
        if password != password2:
            raise serializers.ValidationError('Fields must be equal')
        return attrs


class SettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = '__all__'


class DelayedPackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DelayedAdditionPackage
        fields = ('card_id',
                  'package_id')


class ResellerTieOneCardSerializer(serializers.ModelSerializer):
    cards = CardShortDescriptionSerializer(many=True)

    class Meta:
        model = User
        fields = ('cards',)


class ResellerMakeAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_superuser',)

    def update(self, instance, validated_data):
        instance.is_superuser = validated_data['is_superuser']
        instance.is_staff = validated_data['is_superuser']
        instance.save()
        return instance


class SynchrFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SynchronizeForms
        fields = ('date',
                  'status')
