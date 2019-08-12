from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.signals import Signal
from backend.settings import SSSSS

from .utilities import (
    send_activation_notification,
    send_request_reset_password,
)

user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(**kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)

reset_password = Signal(providing_args=['instance'])


def reset_password_dispatcher(**kwargs):
    send_request_reset_password(kwargs['instance'])


reset_password.connect(reset_password_dispatcher)


class Reseller(AbstractUser):
    address = models.CharField(verbose_name='address', max_length=100, blank=True)
    telephone = models.CharField(verbose_name='telephone', max_length=30, blank=True)
    zone = models.CharField(verbose_name='zone', max_length=50, blank=True)
    rrr = models.CharField(verbose_name='rrr', max_length=3, blank=True)
    balance = models.IntegerField(verbose_name='Balance', default=0)
    credit = models.IntegerField(verbose_name='Credit', default=0)
    price_card = models.IntegerField(verbose_name='Price', default=0)
    comment = models.CharField(verbose_name='Comment', max_length=100, blank=True)
    is_activated = models.BooleanField(verbose_name='Activated', default=True,
                                       db_index=True)

    def __str__(self):
        return self.username or self.email

    class Meta(AbstractUser.Meta):
        pass


User = get_user_model()


def get_admin():
    return User.objects.get(username='admin')


class Bouquet(models.Model):
    number = models.IntegerField(verbose_name='Number', db_index=True, unique=True)
    name = models.CharField(verbose_name='Bouquet', max_length=20)
    age_limit = models.IntegerField(verbose_name='Age limit')
    packages = models.ManyToManyField('Packet', related_name='bouquets')

    def __str__(self):
        return '%d %s' % (self.number, self.name)


class Packet(models.Model):
    header = models.CharField(verbose_name='header', max_length=50, blank=True)
    age_limit = models.IntegerField(verbose_name='Age limit', blank=True, null=True)
    tariff = models.IntegerField(verbose_name='Tariff of one period', default=0)
    cards = models.ForeignKey('Card', on_delete=models.PROTECT, blank=True, null=True,
                              related_name='packages')

    def __str__(self):
        return self.header


class Card(models.Model):
    STATUS = [
        ('Active', 'A'),
        ('Inactive', 'I'),
        ('Expired', 'E'),
    ]
    reseller = models.ForeignKey(User, on_delete=models.PROTECT, default=get_admin, related_name='cards')
    created_at = models.DateTimeField(verbose_name='Created_at', auto_now_add=True)
    last_change = models.DateTimeField(verbose_name='Last_change', auto_now=True, blank=True)
    expired_date = models.DateTimeField(verbose_name='Expired date', blank=True, null=True)
    status = models.CharField(verbose_name='Status', max_length=10, choices=STATUS, default='A')
    subscriber = models.ForeignKey('Subscriber', on_delete=models.PROTECT, related_name='cards',
                                   null=True, blank=True)

    def label(self):
        zero = '000000'
        length = len(str(self.pk))
        nnnnnn = zero[:6-length] + str(self.pk)
        RRR = self.reseller.rrr
        return '{}-{}-{}'.format(SSSSS, str(RRR), nnnnnn)

    def price(self):
        priceReseller = self.reseller.price_card
        if self.packages.exists():
            pricePackages = self.packages.aggregate(
                price=models.Sum('tariff'))['price']
        else:
            pricePackages = 0
        result = priceReseller + pricePackages
        return result

    def __str__(self):
        return '%s %d' % (self.label(), self.pk)


class Subscriber(models.Model):
    first_name = models.CharField(verbose_name='first_name', max_length=50, blank=True)
    last_name = models.CharField(verbose_name='last_name', max_length=50, blank=True)
    address = models.CharField(verbose_name='address', max_length=100, blank=True)
    telephone = models.CharField(verbose_name='telephone', max_length=30, blank=True)
    email = models.EmailField(verbose_name='email', blank=True)
    balance = models.IntegerField(verbose_name='balance', default=0)
    reseller = models.ForeignKey(User, on_delete=models.PROTECT, default=get_admin)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
