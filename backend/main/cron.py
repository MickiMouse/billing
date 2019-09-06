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
    date = datetime.now()
    forms = SynchronizeForms.objects.filter(Q(date__lt=date) & Q(status=False))
    if forms.exists():
        s = Settings.objects.first()
        command = SendCards()
        for card in Card.objects.filter(~Q(subscriber=None) & Q(expired_date__lt=date)):
            connect_package.send(sender=Card, card=card)
            pay_subscription.send(sender=Card, card=card, settings=s)
            command.handle(start=card.pk, stop=card.pk)
        for form in forms:
            form.status = True
            form.save()
        return True
    else:
        for form in forms:
            form.status = False
            form.save()
