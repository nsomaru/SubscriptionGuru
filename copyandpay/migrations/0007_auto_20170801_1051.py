# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-01 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('copyandpay', '0006_auto_20170628_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproduct',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userproduct',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userproduct',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='recurrance_rate',
            field=models.CharField(choices=[('M', 'Monthly'), ('A', 'Annually')], default='M', max_length=22),
        ),
        migrations.AlterField(
            model_name='userproduct',
            name='user',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]