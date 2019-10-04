import datetime
from django.core.management.base import BaseCommand
from django.db.models import Q
from backend.settings import (
    SERVER_LOGIN,
    SERVER_PSWD,
)

from .models import Bouquet, Card, Settings
from .dvcrypt_proto import DVCrypt


class Command(BaseCommand):
    help = 'Get bouquets from server'

    def handle(self, *args, **options):
        settings = Settings.objects.first()
        d = DVCrypt(settings.server_ip, settings.server_port)
        d.connect()
        d.login(SERVER_LOGIN, SERVER_PSWD)
        bouquets = options['count']
        max_bouquets = d.get_bouquet_count()
        detail = {}
        for i in range(bouquets):
            b = d.get_bouquet_detail(i)
            detail[i] = b
        for i in detail:
            obj, created = Bouquet.objects.get_or_create(number=i)
            obj.name = detail[i]['name']
            if created:
                obj.age_limit = detail[i]['parental']
                obj.save()
        for i in range(bouquets, max_bouquets):
            try:
                obj = Bouquet.objects.get(number=i)
                if not obj.packages.exists():
                    obj.delete()
            except Bouquet.DoesNotExist:
                pass
        d.logout()
        d.disconnect()


class SendCards(BaseCommand):
    help = 'Send cards to server'

    def handle(self, *args, **options):
        settings = Settings.objects.first()
        d = DVCrypt(settings.server_ip, settings.server_port)
        d.connect()
        d.login(SERVER_LOGIN, SERVER_PSWD)
        bouquets = set()
        start = options['start']
        stop = options['stop']
        for card in Card.objects.filter(Q(pk__gte=start) & Q(pk__lte=stop)):
            if card.status() == 'Active':
                for package in card.packages.all():
                    for b in package.bouquets.all():
                        bouquets.add(b.number)
                d.subscriber_set(card.pk, card.pk, bouquets, 'low')
                bouquets.clear()
            for package in card.packages.all():
                for b in package.bouquets.all():
                    bouquets.add(b.number)
            d.subscriber_set(card.pk, card.pk, bouquets, 'low')
            bouquets.clear()
        d.logout()
        d.disconnect()

