# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0096_auto_20160624_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]