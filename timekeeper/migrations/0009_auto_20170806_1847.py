# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 23:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timekeeper', '0008_auto_20170725_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectexpenditure',
            name='project_task',
        ),
        migrations.DeleteModel(
            name='ProjectExpenditure',
        ),
    ]