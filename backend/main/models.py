from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.signals import Signal

from .utilities import send_activation_notification

user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(**kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)


class Reseller(AbstractUser):
    address = models.CharField(verbose_name='address', max_length=100, blank=True)
    telephone = models.CharField(verbose_name='telephone', max_length=30, blank=True)
    zone = models.CharField(verbose_name='zone', max_length=50, blank=True)
    rrr = models.CharField(verbose_name='rrr', max_length=3, blank=True)
    score = models.IntegerField(verbose_name='Score', default=0)
    credit = models.IntegerField(verbose_name='Credit', default=0)
    price_card = models.IntegerField(verbose_name='Price', default=0)
    comment = models.CharField(verbose_name='Comment', max_length=100, blank=True)
    is_activated = models.BooleanField(verbose_name='Activated', default=True,
                                       db_index=True)

    class Meta(AbstractUser.Meta):
        pass


User = get_user_model()


class Packet(models.Model):
    header = models.CharField(verbose_name='header', max_length=50, blank=True)


class Card(models.Model):
    reseller = models.ForeignKey(User, on_delete=models.PROTECT)
    packet = models.ForeignKey(Packet, on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='created_at', default=timezone.now)
    last_change = models.DateTimeField(verbose_name='last_change', auto_now=True, blank=True)
    expired_date = models.DateTimeField(verbose_name='expired')
    status = models.BooleanField(verbose_name='status', default=True)
    subscriber = models.ForeignKey('Subscriber', on_delete=models.PROTECT, null=True)


class Subscriber(models.Model):
    first_name = models.CharField(verbose_name='first_name', max_length=50, blank=True)
    last_name = models.CharField(verbose_name='last_name', max_length=50, blank=True)
    reseller = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.CharField(verbose_name='address', max_length=100, blank=True)
    telephone = models.CharField(verbose_name='telephone', max_length=30, blank=True)
    email = models.EmailField(verbose_name='email', blank=True)
    score = models.IntegerField(verbose_name='score', default=0)
