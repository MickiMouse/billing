from datetime import datetime
from dateutil.relativedelta import relativedelta
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

pay_subscription = Signal(providing_args=['card', 'settings'])


def pay_subscription_dispatcher(**kwargs):
    card = kwargs['card']
    settings = kwargs['settings']
    subscriber = card.subscriber
    if subscriber is None:
        return 'Inactive'
    diff = subscriber.balance - card.price()
    if diff < 0:
        return 'Expired'
    subscriber.balance -= card.price()
    period = settings.quantity
    if settings.kind_period == 'MONTHS':
        card.expired_date = datetime.now() + relativedelta(months=period)
    elif settings.kind_period == 'WEEKS':
        card.expired_date = datetime.now() + relativedelta(weeks=period)
    else:
        card.expired_date = datetime.now() + relativedelta(minutes=period)
    subscriber.save(update_fields=['balance'])
    card.save(update_fields=['expired_date'])


pay_subscription.connect(pay_subscription_dispatcher)


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
    return User.objects.get(username='admin').pk


class Bouquet(models.Model):
    number = models.IntegerField(verbose_name='Number', db_index=True, unique=True)
    name = models.CharField(verbose_name='Bouquet', max_length=20, blank=True, null=True)
    age_limit = models.IntegerField(verbose_name='Age limit',
                                    blank=True, null=True)
    packages = models.ManyToManyField('Packet', blank=True, null=True,
                                      related_name='bouquets')

    def __str__(self):
        return '%d %s' % (self.number, self.name)


class Packet(models.Model):
    header = models.CharField(verbose_name='header', max_length=50)
    tariff = models.IntegerField(verbose_name='Tariff of one period', default=0)
    cards = models.ManyToManyField('Card', blank=True, null=True,
                                   related_name='packages')

    def age_limit(self):
        age = self.bouquets.aggregate(
            max=models.Max('age_limit'))['max']
        return age

    def __str__(self):
        return self.header


class Card(models.Model):
    reseller = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_admin, related_name='cards')
    created_at = models.DateTimeField(verbose_name='Created_at', auto_now_add=True)
    last_change = models.DateTimeField(verbose_name='Last_change', auto_now=True, blank=True)
    expired_date = models.DateTimeField(verbose_name='Expired date', blank=True, null=True)
    subscriber = models.ForeignKey('Subscriber', on_delete=models.PROTECT, related_name='cards',
                                   null=True, blank=True)

    def label(self):
        zero = '000000'
        length = len(str(self.pk))
        nnnnnn = zero[:6-length] + str(self.pk)
        RRR = self.reseller.rrr
        return '{}-{}-{}'.format(SSSSS, str(RRR), nnnnnn)

    def price(self):
        if self.packages.exists():
            pricePackages = self.packages.aggregate(
                price=models.Sum('tariff'))['price']
        else:
            pricePackages = 0
        return pricePackages

    def status(self):
        if self.expired_date is None:
            return 'Inactive'
        else:
            if self.expired_date > datetime.now():
                return 'Active'
            else:
                settings = Settings.objects.first()
                if settings.kind_payment == 'VIRTUAL':
                    pay_subscription.send(sender=Card, card=self,
                                          settings=settings)
                return 'Expired'

    def __str__(self):
        return '%s %d' % (self.label(), self.pk)


class Subscriber(models.Model):
    first_name = models.CharField(verbose_name='first_name', max_length=50, blank=True)
    last_name = models.CharField(verbose_name='last_name', max_length=50, blank=True)
    address = models.CharField(verbose_name='address', max_length=100, blank=True)
    telephone = models.CharField(verbose_name='telephone', max_length=30, blank=True)
    email = models.EmailField(verbose_name='email', blank=True)
    balance = models.IntegerField(verbose_name='balance', default=0)
    reseller = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_admin)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Settings(models.Model):
    kind_payment = models.CharField(verbose_name='payment', max_length=10, default='PREPAYMENT')
    kind_period = models.CharField(verbose_name='period', max_length=10, default='MONTHS')
    quantity = models.IntegerField(verbose_name='quantity', default=1)
