# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20170507_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationships',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relationships',
            name='attribute',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
