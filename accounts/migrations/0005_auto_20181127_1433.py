# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-27 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181127_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]