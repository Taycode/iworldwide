# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-09 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20180509_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profile_image/whatsapponpc.png', upload_to='profile_image'),
        ),
    ]
