# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-12 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='ans',
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='formApp.Questions'),
        ),
    ]
