# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 19:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('project_description', models.TextField(max_length=200)),
                ('project_hours', models.IntegerField(default=0)),
                ('flat_rate', models.BooleanField(default=False)),
                ('running_cost', models.FloatField(default=0)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timekeeper.Client')),
                ('employees', models.ManyToManyField(related_name='employees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_task_title', models.CharField(max_length=50)),
                ('project_task_description', models.CharField(max_length=200)),
                ('project_task_hours_remaining', models.IntegerField()),
                ('project_task_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='timekeeper.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Timecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timecard_date', models.DateField()),
                ('timecard_hours', models.IntegerField(default=0)),
                ('timecard_charge', models.FloatField(default=0)),
                ('timecard_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('timecard_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timekeeper.Project')),
            ],
        ),
    ]