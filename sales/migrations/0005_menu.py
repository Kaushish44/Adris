# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-17 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20170819_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('category', models.IntegerField()),
            ],
        ),
    ]
