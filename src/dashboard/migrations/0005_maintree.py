# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-26 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_relationships_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.IntegerField(blank=True, null=True)),
                ('relations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.relationships')),
            ],
        ),
    ]
