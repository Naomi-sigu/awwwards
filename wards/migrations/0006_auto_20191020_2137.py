# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-20 18:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0005_auto_20191020_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_image',
            new_name='image',
        ),
    ]
