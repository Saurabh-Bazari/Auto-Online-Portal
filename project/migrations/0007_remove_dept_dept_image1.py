# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_facility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dept',
            name='Dept_image1',
        ),
    ]
