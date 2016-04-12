# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('R', 'Regular'), ('PT', 'Part Time'), ('P', 'Probationary'), ('I', 'Intern'), ('T', 'Terminated'), ('A', 'Admin')], max_length=2),
        ),
    ]
