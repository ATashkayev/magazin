# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0006_auto_20171013_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructors',
            name='who_i_am',
        ),
        migrations.AddField(
            model_name='instructors',
            name='who_i_am_s',
            field=models.ManyToManyField(to='instructor.Spisok'),
        ),
    ]
