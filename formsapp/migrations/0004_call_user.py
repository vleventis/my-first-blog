# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 20:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0003_auto_20170226_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]