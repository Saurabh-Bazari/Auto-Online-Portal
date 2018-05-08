# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 15:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20171114_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_dept',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_position',
            new_name='Designation',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_ri',
            new_name='Research_Interests',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_room',
            new_name='Room_No',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_address1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_address2',
            new_name='address2',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_phoneo',
            new_name='phone_office',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='Prof_phoner',
            new_name='phone_r',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Project_detail',
            new_name='Detail',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Project_Funding_agency',
            new_name='Funding_agency',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Project_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Project_prof',
            new_name='Professor',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='Publication_detail',
            new_name='Detail',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='Publication_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='Publication_prof',
            new_name='Professor',
        ),
        migrations.RenameField(
            model_name='recognition',
            old_name='Recognition_detail',
            new_name='Detail',
        ),
        migrations.RenameField(
            model_name='recognition',
            old_name='Recognition_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='recognition',
            old_name='Recognition_prof',
            new_name='Professor',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_detail',
            new_name='Detail',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_prof',
            new_name='Professor',
        ),
        migrations.RenameField(
            model_name='teaching',
            old_name='Teaching_detail',
            new_name='Detail',
        ),
        migrations.RenameField(
            model_name='teaching',
            old_name='Teaching_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='teaching',
            old_name='Teaching_prof',
            new_name='Professor',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='recognition',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='teaching',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='teaching',
            name='start_date',
        ),
        migrations.AddField(
            model_name='project',
            name='End_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 15, 2, 32, 47849)),
        ),
        migrations.AddField(
            model_name='project',
            name='Start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 15, 2, 32, 47827)),
        ),
        migrations.AddField(
            model_name='publication',
            name='Date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 15, 2, 32, 45177)),
        ),
        migrations.AddField(
            model_name='recognition',
            name='Date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 15, 2, 32, 45583)),
        ),
        migrations.AddField(
            model_name='student',
            name='End_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 15, 2, 32, 45995)),
        ),
        migrations.AddField(
            model_name='student',
            name='Start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 15, 2, 32, 45974)),
        ),
        migrations.AddField(
            model_name='teaching',
            name='End_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 15, 2, 32, 47340)),
        ),
        migrations.AddField(
            model_name='teaching',
            name='Start_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 15, 2, 32, 47318)),
        ),
    ]
