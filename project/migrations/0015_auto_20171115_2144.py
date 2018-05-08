# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 21:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20171115_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Funding_agency', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Detail', models.CharField(max_length=10000)),
                ('Start_date', models.DateField(default=datetime.datetime(2017, 11, 15, 21, 44, 12, 62800))),
                ('End_date', models.DateField(default=datetime.datetime(2017, 11, 15, 21, 44, 12, 62821))),
                ('Professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Prof')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='Professor',
        ),
        migrations.AlterField(
            model_name='publication',
            name='Date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 21, 44, 12, 60254)),
        ),
        migrations.AlterField(
            model_name='recognition',
            name='Date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 21, 44, 12, 60674)),
        ),
        migrations.AlterField(
            model_name='student',
            name='End_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 21, 44, 12, 61105)),
        ),
        migrations.AlterField(
            model_name='student',
            name='Start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 21, 44, 12, 61084)),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='End_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 21, 44, 12, 62316)),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='Start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 21, 44, 12, 62296)),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
