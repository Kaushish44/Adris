# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-24 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='food_ordered',
            field=models.CharField(max_length=900),
        ),
    ]
