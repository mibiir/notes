# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20171126_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='logo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
