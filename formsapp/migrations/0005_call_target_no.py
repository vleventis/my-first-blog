# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0004_call_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='target_no',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]