# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksmanager', '0003_publisher_addr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='addr',
            field=models.CharField(max_length=128),
        ),
    ]
