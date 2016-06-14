# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='hometown',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
