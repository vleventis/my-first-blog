# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 01:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0007_auto_20170226_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='timeofcall',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 27, 1, 13, 11, 349088, tzinfo=utc)),
        ),
    ]
