# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-27 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181127_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
