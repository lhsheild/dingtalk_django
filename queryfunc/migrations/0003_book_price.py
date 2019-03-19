# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-19 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryfunc', '0002_auto_20190319_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=99.99, max_digits=5),
        ),
    ]
