# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20171107_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Группы товара')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Остатки размеров'),
        ),
        migrations.AddField(
            model_name='products',
            name='group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductGroup'),
        ),
    ]