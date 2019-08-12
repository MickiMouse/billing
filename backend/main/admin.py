from django.contrib import admin

from .models import (
    Reseller,
    Card,
    Packet,
    Subscriber,
    Bouquet,
)


class ResellerAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'rrr', 'balance', 'is_activated')


class CardAdmin(admin.ModelAdmin):
    list_display = ('label', 'reseller', 'price',
                    'expired_date', 'status')


class BouquetAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'age_limit')


admin.site.register(Reseller, ResellerAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Packet)
admin.site.register(Subscriber)
admin.site.register(Bouquet, BouquetAdmin)
