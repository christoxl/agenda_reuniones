# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20171011_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sesions', to='web.Entidad'),
        ),
    ]
