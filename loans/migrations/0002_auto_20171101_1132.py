# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='date_req',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='pictures',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
