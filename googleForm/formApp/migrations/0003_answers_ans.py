# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-12 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formApp', '0002_auto_20171113_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='ans',
            field=models.TextField(default=0),
        ),
    ]