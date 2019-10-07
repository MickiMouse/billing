from datetime import datetime
from django.db.models import Q

from .models import (
    Card,
    Settings,
    SynchronizeForms,
    pay_subscription,
    connect_package)
from .api import SendCards


def my_scheduled_job():
    date = datetime.now().time()
    forms = SynchronizeForms.objects.filter(date__lte=date)
    if forms.exists():
        s = Settings.objects.first()
        command = SendCards()
        _date = datetime.now()
        for card in Card.objects.filter(~Q(subscriber=None)):
            if card.status() == 'Expired':
                subscriber = card.subscriber
                if s.kind_payment == 'VIRTUAL':
                    if subscriber.balance - card.price() >= 0:
                        pay_subscription.send(sender=Card, card=card, settings=s)
                connect_package.send(sender=Card, card=card)
                # command.handle(start=card.pk, stop=card.pk)
        for form in forms:
            form.status = True
            form.save()
