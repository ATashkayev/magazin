from django.contrib import admin

# Register your models here.
from products.models import *

class ProductImageInline(admin.TabularInline):
    model = Spisok_foto

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    class Meta:
        model = Products

admin.site.register(Products, ProductAdmin)
admin.site.register(Spisok_foto)
admin.site.register(ProductGroup)
