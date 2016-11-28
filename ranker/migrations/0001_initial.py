# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ranker.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('image_b', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('image_c', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('image_d', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ItemView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=ranker.util.datetime_now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranker.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WishListEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=ranker.util.datetime_now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranker.Item')),
                ('wish_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranker.WishList')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranker.Seller'),
        ),
    ]