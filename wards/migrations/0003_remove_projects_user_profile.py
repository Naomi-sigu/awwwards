# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-20 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0002_auto_20191020_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='user_profile',
        ),
    ]
