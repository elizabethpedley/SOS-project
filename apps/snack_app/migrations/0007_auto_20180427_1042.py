# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-27 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack_app', '0006_auto_20180426_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.ImageField(upload_to='.static/images/'),
        ),
    ]
