# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20171127_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='logo',
            field=models.ImageField(blank=True, default='', upload_to=''),
            preserve_default=False,
        ),
    ]
