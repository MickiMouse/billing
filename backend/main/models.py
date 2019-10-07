from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.signals import Signal

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
    continue_subscription(card=kwargs['card'], settings=kwargs['settings'])


pay_subscription.connect(pay_subscription_dispatcher)

connect_package = Signal(providing_args=['card'])


def connect_package_dispatcher(**kwargs):
    delayed_connect_package(card=kwargs['card'])


connect_package.connect(connect_package_dispatcher)


class Reseller(AbstractUser):
    address = models.CharField(verbose_name='address', max_length=100, blank=True)
    telephone = models.CharField(verbose_name='telephone', max_length=30, blank=True)
    zone = models.CharField(verbose_name='zone', max_length=50, blank=True)
    balance = models.FloatField(verbose_name='Balance', default=0)
    credit = models.FloatField(verbose_name='Credit', default=0)
    price_card = models.FloatField(verbose_name='Price', default=0)
    comment = models.CharField(verbose_name='Comment', max_length=100, blank=True)
    is_activated = models.BooleanField(verbose_name='Activated', default=True,
                                       db_index=True)
    rrr = models.CharField(verbose_name='Prefix', max_length=3, blank=True)
    is_confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.username or self.email

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.rrr = '000'
        super().save(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass


User = get_user_model()


def get_admin():
    return User.objects.get(is_superuser=True).pk


class Bouquet(models.Model):
    number = models.IntegerField(verbose_name='Number', db_index=True, unique=True)
    name = models.CharField(verbose_name='Bouquet', max_length=20, blank=True, null=True)
    age_limit = models.IntegerField(verbose_name='Age limit', blank=True, null=True)
    packages = models.ManyToManyField('Packet', blank=True, null=True,
                                      related_name='bouquets')

    def __str__(self):
        return '%d %s' % (self.number, self.name)


class Packet(models.Model):
    header = models.CharField(verbose_name='header', max_length=50, blank=True, null=True)
    tariff = models.FloatField(verbose_name='Tariff of one period', default=0, blank=True, null=True)
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
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    last_change = models.DateTimeField(verbose_name='Last change', auto_now=True, blank=True)
    expired_date = models.DateTimeField(verbose_name='Expired date', blank=True, null=True)
    subscriber = models.ForeignKey('Subscriber', on_delete=models.PROTECT, related_name='cards',
                                   null=True, blank=True)
    suspend_date = models.DateTimeField(verbose_name='Suspend date', blank=True, null=True)
    suspend = models.BooleanField(verbose_name='Suspend', default=False, db_index=True)

    def label(self):
        zero = '000000'
        length = len(str(self.pk))
        nnnnnn = zero[:6-length] + str(self.pk)
        RRR = self.reseller.rrr
        settings = Settings.objects.first()
        return '{}-{}-{}'.format(settings.sssss, str(RRR), nnnnnn)

    def price(self):
        if self.packages.exists():
            pricePackages = self.packages.aggregate(
                price=models.Sum('tariff'))['price']
        else:
            pricePackages = 0
        return pricePackages + self.reseller.price_card

    def status(self):
        if self.expired_date is None or self.subscriber is None:
            return 'Inactive'
        elif self.suspend:
            return 'Suspend'
        else:
            if self.expired_date > datetime.now():
                return 'Active'
            else:
                return 'Expired'

    def suspend_interval(self):
        return relativedelta(dt1=self.expired_date, dt2=self.suspend_date)

    def delete_date(self):
        return self.created_at + relativedelta(days=3)

    def __str__(self):
        return '%s %d' % (self.label(), self.pk)

    class Meta:
        ordering = ['created_at']


class Subscriber(models.Model):
    first_name = models.CharField(verbose_name='first_name', max_length=50, blank=True, null=True)
    last_name = models.CharField(verbose_name='last_name', max_length=50, blank=True, null=True)
    address = models.CharField(verbose_name='address', max_length=100, blank=True, null=True)
    telephone = models.CharField(verbose_name='telephone', max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='email', blank=True, null=True)
    balance = models.IntegerField(verbose_name='balance', default=0)
    reseller = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_admin)
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['created_at']


class Settings(models.Model):
    server_ip = models.CharField(verbose_name='IP server', max_length=16, blank=True, null=True)
    server_port = models.IntegerField(verbose_name='Port', null=True)
    max_cards = models.IntegerField(verbose_name='Max count cards', default=100000)
    sssss = models.CharField(verbose_name='Prefix system', max_length=5, default='00000')
    currency = models.CharField(verbose_name='Currency', max_length=100, default='$')
    kind_payment = models.CharField(verbose_name='payment', max_length=10, default='PREPAYMENT')
    kind_period = models.CharField(verbose_name='period', max_length=10, default='MONTHS')
    quantity = models.IntegerField(verbose_name='quantity', default=1)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)


class Logs(models.Model):
    log = models.CharField(verbose_name='Log', max_length=200, blank=True, null=True)
    date = models.DateTimeField(verbose_name='Created', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['date']
        get_latest_by = ['date']


class LogsCard(Logs):
    card = models.ForeignKey(Card, on_delete=models.PROTECT, related_name='logs',
                             null=True, blank=True)

    class Meta(Logs.Meta):
        pass


class LogsSubscriber(Logs):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.PROTECT, related_name='logs',
                                   null=True, blank=True)

    class Meta(Logs.Meta):
        pass


class LogsReseller(Logs):
    reseller = models.ForeignKey(User, on_delete=models.PROTECT, related_name='logs',
                                 null=True, blank=True)

    class Meta(Logs.Meta):
        pass


class DelayedAdditionPackage(models.Model):
    card_id = models.IntegerField(verbose_name='Card')
    package_id = models.IntegerField(verbose_name='Package')

    def __str__(self):
        return '%d %d' % (self.card_id, self.package_id)


class DelayedRemovePackage(models.Model):
    card_id = models.IntegerField(verbose_name='Card')
    package_id = models.IntegerField(verbose_name='Package')

    def __str__(self):
        return '%d %d' % (self.card_id, self.package_id)


class ReportSubscription(models.Model):
    subscription = models.IntegerField(verbose_name='Count sub', db_index=True, default=0)
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    reseller = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reports')

    class Meta:
        ordering = ['created_at']
        get_latest_by = ['created_at']


class ReportFinance(models.Model):
    spend_money = models.IntegerField(verbose_name='Money', db_index=True, default=0)
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    reseller = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reports_finance')

    class Meta:
        ordering = ['created_at']
        get_latest_by = ['created_at']


class SynchronizeForms(models.Model):
    date = models.TimeField(verbose_name='Time to synchronize', null=True)
    status = models.BooleanField(verbose_name='Completed?', default=False)

    class Meta:
        ordering = ['date']


from .utilities import (
    send_activation_notification,
    send_request_reset_password,
    continue_subscription,
    delayed_connect_package
)
