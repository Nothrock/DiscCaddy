# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20171117_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckInImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('check_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pages.CheckIn')),
            ],
        ),
    ]
