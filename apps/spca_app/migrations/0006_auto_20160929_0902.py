# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spca_app', '0005_auto_20160928_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.CharField(max_length=45),
        ),
    ]