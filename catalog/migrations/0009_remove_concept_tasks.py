# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-20 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20171220_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concept',
            name='tasks',
        ),
    ]