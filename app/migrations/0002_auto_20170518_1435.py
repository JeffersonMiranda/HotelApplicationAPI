# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-18 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='employee',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Employee'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='occupation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Occupation'),
        ),
    ]
