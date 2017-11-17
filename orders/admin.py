from django.contrib import admin

# Register your models here.
from orders.models import *


class ProductInOrderInline(admin.TabularInline):

    model = ProductInOrder

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

admin.site.register(ProductInOrder)

admin.site.register(ProductInBasket)

admin.site.register(OrderInSession)