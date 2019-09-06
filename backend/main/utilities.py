from dateutil.relativedelta import relativedelta
from django.template.loader import render_to_string
from django.core.signing import Signer
from django.core.mail import send_mail

from .models import (
    Packet,
    DelayedRemovePackage,
    DelayedAdditionPackage,
    Settings,
    LogsCard,
    LogsSubscriber,
)

signer = Signer()

from .views import logging


def send_activation_notification(user):
    settings = Settings.objects.first()
    host = f'http://localhost:8080/login/{signer.sign(user.email)}'
    context = {'user': user, 'host': host}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body = render_to_string('email/activation_letter_body.txt', context)
    send_mail(subject, body, settings.email, [user.email])


def send_request_reset_password(user):
    settings = Settings.objects.first()
    host = f'http://localhost:8080/password/{signer.sign(user.email)}'
    context = {'user': user, 'host': host,
               'sign': signer.sign(user.email)}
    subject = render_to_string('email/reset_password_subject.txt', context)
    body = render_to_string('email/reset_password_body.txt', context)
    send_mail(subject, body, settings.email, [user.email])


def continue_subscription(card, settings):
    if settings.kind_payment == 'VIRTUAL':
        subscriber = card.subscriber
        diff = subscriber.balance - card.price()

        if diff < 0:
            return

        subscriber.balance -= card.price()
        period = settings.quantity

        if settings.kind_period == 'MONTHS':
            card.expired_date = card.expired_date + relativedelta(months=period)
        elif settings.kind_period == 'WEEKS':
            card.expired_date = card.expired_date + relativedelta(weeks=period)
        else:
            card.expired_date = card.expired_date + relativedelta(days=period)

        subscriber.save(update_fields=['balance'])
        card.save(update_fields=['expired_date'])

        log = 'ID SUBSCRIBER: {}; LOG: Payed. Price - {}; Balance - {};'
        logging(LogsSubscriber, subscriber, log, subscriber.balance, card.price())
        log = 'ID CARD: {}; LOG: Update expired date {};'
        logging(LogsCard, card, log, card.expired_date)


def delayed_connect_package(card):
    _packages = list(card.packages.all())
    delayedAdd = DelayedAdditionPackage.objects.filter(card_id=card.pk)
    if delayedAdd.exists():
        for pack in delayedAdd:
            package = Packet.objects.get(pk=pack.package_id)
            _packages.append(package)
            log = 'ID CARD: {}; LOG: Add package {};'
            logging(LogsCard, card, log, package.header)
            pack.delete()
        card.packages.set(_packages)
        card.save()

    delayedRemove = DelayedRemovePackage.objects.filter(card_id=card.pk)
    if delayedRemove.exists():
        for pack in delayedRemove:
            package = Packet.objects.get(pk=pack.package_id)
            try:
                _packages.remove(package)
                log = 'ID CARD: {}; LOG: Remove package {};'
                logging(LogsCard, card, log, package.header)
            except ValueError:
                pass
            pack.delete()
        card.packages.set(_packages)
        card.save()
