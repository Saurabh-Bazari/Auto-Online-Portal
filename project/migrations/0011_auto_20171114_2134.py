# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 21:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20171114_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 21, 34, 52, 123849)),
        ),
        migrations.AddField(
            model_name='publication',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 21, 34, 52, 122121)),
        ),
        migrations.AddField(
            model_name='recognition',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 21, 34, 52, 122526)),
        ),
        migrations.AddField(
            model_name='student',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 21, 34, 52, 122931)),
        ),
        migrations.AddField(
            model_name='student',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 21, 34, 52, 122913)),
        ),
        migrations.AddField(
            model_name='teaching',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 21, 34, 52, 123441)),
        ),
        migrations.AddField(
            model_name='teaching',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 21, 34, 52, 123422)),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 21, 34, 52, 123868)),
        ),
    ]