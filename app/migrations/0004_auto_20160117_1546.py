# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160117_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'Ponente'},
        ),
    ]
