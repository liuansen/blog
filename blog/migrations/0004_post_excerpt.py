# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-18 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171018_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200, verbose_name='摘要'),
        ),
    ]
