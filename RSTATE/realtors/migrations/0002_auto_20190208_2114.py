# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-02-08 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Realtors',
            new_name='Realtor',
        ),
    ]
