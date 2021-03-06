# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whisper', '0004_auto_20170226_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secret',
            old_name='message',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='secret',
            name='likes',
            field=models.ManyToManyField(related_name='liked', to='whisper.User'),
        ),
    ]
