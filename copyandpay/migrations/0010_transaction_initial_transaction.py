# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-27 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copyandpay', '0009_auto_20170927_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='initial_transaction',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='copyandpay.Transaction'),
        ),
    ]
