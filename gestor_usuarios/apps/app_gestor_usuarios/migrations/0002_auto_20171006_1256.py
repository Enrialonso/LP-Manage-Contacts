# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestor_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_manage_contacts',
            name='state',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='db_manage_contacts',
            name='street_number',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
