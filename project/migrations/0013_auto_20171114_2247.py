# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 22:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20171114_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 22, 47, 5, 269880)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 22, 47, 5, 269859)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 22, 47, 5, 267503)),
        ),
        migrations.AlterField(
            model_name='recognition',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 22, 47, 5, 267914)),
        ),
        migrations.AlterField(
            model_name='student',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 22, 47, 5, 268326)),
        ),
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 22, 47, 5, 268306)),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 22, 47, 5, 269437)),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 22, 47, 5, 269418)),
        ),
    ]
