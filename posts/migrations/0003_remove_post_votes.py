# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20161203_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
    ]