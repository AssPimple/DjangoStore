from django.contrib import admin

from orders.models import OrderModel


# Register your models here.
@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status',)
    fields = (
        'id', 'created',
        ('first_name', 'last_name'),
        ('email', 'address'),
        'basket_history', 'status', 'initiator',
    )
    readonly_fields = ('id', 'created')
