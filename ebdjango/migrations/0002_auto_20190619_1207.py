# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-06-19 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebdjango', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tvsetting',
            old_name='cos',
            new_name='themeURL',
        ),
    ]
