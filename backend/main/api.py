from django.core.management.base import BaseCommand
from backend.settings import (
    SERVER_IP,
    SERVER_PORT,
    SERVER_LOGIN,
    SERVER_PSWD,
)

from .models import Bouquet
from .dvcrypt_proto import DVCrypt


class Command(BaseCommand):
    help = 'Get bouquets from server'

    def handle(self, *args, **options):
        d = DVCrypt(SERVER_IP, SERVER_PORT)
        d.connect()
        d.login(SERVER_LOGIN, SERVER_PSWD)
        bouquets = options['count']
        max_bouquets = d.get_bouquet_count()
        detail = {}
        for i in range(0, bouquets):
            b = d.get_bouquet_detail(i)
            detail[i] = b
        for i in detail:
            obj, created = Bouquet.objects.get_or_create(number=i)
            if created:
                obj.name = detail[i]['name']
                obj.age_limit = detail[i]['parental']
                obj.save()
                print(obj.name)
                print(obj.age_limit)
                print('SAVED')
        for i in range(bouquets, max_bouquets):
            try:
                obj = Bouquet.objects.get(number=i)
                if not obj.packages.exists():
                    obj.delete()
            except Bouquet.DoesNotExist:
                pass
        d.logout()
        d.disconnect()
