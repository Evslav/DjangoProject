# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 00:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20170918_0303'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userInfo',
            new_name='uInfo',
        ),
    ]