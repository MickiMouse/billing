from django.contrib import admin

from .models import Reseller, Card, Packet, Subscriber

admin.site.register(Reseller)
admin.site.register(Card)
admin.site.register(Packet)
admin.site.register(Subscriber)
