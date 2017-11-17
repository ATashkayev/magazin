from django.db import models
from products.models import Products
from django.db.models.signals import post_save
from decimal import *


class Order(models.Model):
    customer_name = models.CharField(max_length=60, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=25, blank=True, null=True, default=None)
    customer_adress = models.CharField(max_length=254, blank=True, null=True, default=None)
    coments = models.CharField(max_length=254, blank=True, null=True, default=None)

    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # total price of orders


    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return "Заказ %s" % self.id


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Products, blank=True, null=True, default=None)
    numb = models.IntegerField(default=1)

    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # price * numb

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.total_amount = self.numb * self.price
        super(ProductInOrder, self).save(*args, **kwargs)


def ufter_save(sender, instance, created, **kwargs):
    order = instance.order
    all_pro_in_order = ProductInOrder.objects.filter(order=order)
    total = 0
    for item in all_pro_in_order:
        total += item.total_amount
    instance.order.total_amount = total
    instance.order.save(force_update=True)


post_save.connect(ufter_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=123)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Products, blank=True, null=True, default=None)
    numb = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # price * numb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.total_amount = int(self.numb) * Decimal(self.price)
        super(ProductInBasket, self).save(*args, **kwargs)

class OrderInSession(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=123)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    def __str__(self):
        return " %s" % self.order

    class Meta:
        verbose_name = 'Заказ в сесии'
        verbose_name_plural = 'Заказы в сесии'