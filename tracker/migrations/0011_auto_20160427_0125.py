# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20160427_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
