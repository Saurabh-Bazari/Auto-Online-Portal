# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 22:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20171115_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expreience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Detail', models.CharField(max_length=10000)),
                ('Start_date', models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 663633))),
                ('End_date', models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 663653))),
            ],
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='phone_r',
            new_name='phone_residency',
        ),
        migrations.AlterField(
            model_name='projects',
            name='End_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 663231)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='Start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 663210)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='Date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 660824)),
        ),
        migrations.AlterField(
            model_name='recognition',
            name='Date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 661230)),
        ),
        migrations.AlterField(
            model_name='student',
            name='End_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 661641)),
        ),
        migrations.AlterField(
            model_name='student',
            name='Start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 661622)),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='End_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 662797)),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='Start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 22, 47, 20, 662777)),
        ),
        migrations.AddField(
            model_name='expreience',
            name='Professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Prof'),
        ),
    ]
