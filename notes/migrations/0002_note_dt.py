# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='dt',
            field=models.DateTimeField(null=True),
        ),
    ]
