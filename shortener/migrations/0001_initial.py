# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-23 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KirrURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=220)),
                ('shortcode', models.CharField(max_length=15, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestap', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
