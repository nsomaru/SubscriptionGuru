# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('copyandpay', '0002_remove_transaction_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='registration_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=42),
            preserve_default=False,
        ),
    ]