# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-26 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack_app', '0005_auto_20180425_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
