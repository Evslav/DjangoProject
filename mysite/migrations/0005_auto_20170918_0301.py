# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 00:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='user_agent',
        ),
    ]