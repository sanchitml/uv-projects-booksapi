# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-30 06:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='search_endmpoint',
        ),
    ]
