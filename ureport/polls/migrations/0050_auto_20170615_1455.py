# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0049_auto_20170613_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollresultscounter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]