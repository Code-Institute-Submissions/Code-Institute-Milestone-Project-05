# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-17 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysitters', '0004_reference_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reference',
            old_name='family',
            new_name='refFamily',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='referenceText',
            new_name='reference',
        ),
        migrations.AddField(
            model_name='reference',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
