# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timekeeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='project_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timekeeper.ProjectTask'),
        ),
    ]