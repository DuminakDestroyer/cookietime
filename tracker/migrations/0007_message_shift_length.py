# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20160426_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='shift_length',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
    ]
