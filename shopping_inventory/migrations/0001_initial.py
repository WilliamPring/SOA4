# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('po_number', models.CharField(max_length=50)),
                ('order_date', models.CharField(max_length=50)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_inventory.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('prod_weight', models.FloatField()),
                ('in_stock', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='cust_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_inventory.Customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='prod_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_inventory.Product'),
        ),
    ]
