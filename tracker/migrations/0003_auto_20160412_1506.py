# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='account',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
