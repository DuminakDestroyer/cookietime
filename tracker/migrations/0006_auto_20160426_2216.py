# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='shift_length',
            new_name='message_id',
        ),
    ]
