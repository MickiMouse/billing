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
    forms = SynchronizeForms.objects.filter(Q(date__lt=datetime.now()) & Q(status=False))
    if forms.exists():
        s = Settings.objects.first()
        command = SendCards()
        for card in Card.objects.filter(~Q(subscriber=None) & Q(expired_date__lt=datetime.now())):
            connect_package.send(sender=Card, card=card)
            pay_subscription.send(sender=Card, card=card, settings=s)
            command.handle(start=card.pk, stop=card.pk)
        for form in forms:
            form.delete()
        return True
