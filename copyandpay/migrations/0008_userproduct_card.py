# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-01 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copyandpay', '0007_auto_20170801_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproduct',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='copyandpay.CreditCard'),
        ),
    ]
