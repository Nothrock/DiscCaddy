# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pdga_number',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
