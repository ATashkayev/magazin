# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='min_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, verbose_name='Закупочная цена товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Остаток товара'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, verbose_name='Цена товара'),
        ),
    ]
