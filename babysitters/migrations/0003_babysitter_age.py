# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-26 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysitters', '0002_babysitter_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='babysitter',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
    ]