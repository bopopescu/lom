# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-12 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20171212_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='code',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='code',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
