# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-17 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysitters', '0005_auto_20181117_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='graduated',
            field=models.BooleanField(default=False),
        ),
    ]
