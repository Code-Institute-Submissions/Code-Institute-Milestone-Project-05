# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-17 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babysitters', '0003_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('referenceText', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('babysitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babysitters.Babysitter')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField(blank=True, null=True)),
                ('current', models.BooleanField(default=False)),
                ('babysitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babysitters.Babysitter')),
            ],
        ),
    ]
