# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160117_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='bio',
            field=models.TextField(verbose_name='Bio'),
        ),
    ]
