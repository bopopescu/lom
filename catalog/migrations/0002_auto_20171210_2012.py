# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-10 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='catalog.Task'),
        ),
    ]
