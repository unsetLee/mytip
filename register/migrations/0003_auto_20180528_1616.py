# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-28 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20180528_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='register',
            name='agree',
            field=models.CharField(choices=[('Y', '예'), ('N', '아니오')], default='N', max_length=5),
        ),
    ]
