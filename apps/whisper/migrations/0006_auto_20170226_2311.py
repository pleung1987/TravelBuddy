# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whisper', '0005_auto_20170226_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='secret',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='secret',
            name='likes',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.DeleteModel(
            name='Secret',
        ),
        migrations.AddField(
            model_name='travel',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planner', to='whisper.User'),
        ),
        migrations.AddField(
            model_name='travel',
            name='join',
            field=models.ManyToManyField(related_name='joiner', to='whisper.User'),
        ),
    ]
