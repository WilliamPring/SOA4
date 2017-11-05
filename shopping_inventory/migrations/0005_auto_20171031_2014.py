# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_inventory', '0004_auto_20171029_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping_inventory.Order'),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cust_id',
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set([('order_id', 'prod_id')]),
        ),
    ]
