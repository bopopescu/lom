# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-08 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('tlt', models.CharField(max_length=200)),
                ('public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('tlt', models.CharField(max_length=200)),
                ('concepts', models.ManyToManyField(to='catalog.Concept')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tlt', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('tlt', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='concept',
            name='tags',
            field=models.ManyToManyField(to='catalog.Tag'),
        ),
        migrations.AddField(
            model_name='concept',
            name='tasks',
            field=models.ManyToManyField(to='catalog.Task'),
        ),
    ]