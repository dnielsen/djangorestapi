# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 17:12
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={},
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='created',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='code',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='title',
        ),
        migrations.AddField(
            model_name='snippet',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='snippet',
            name='label',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='snippet',
            name='swipe_val',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='snippet',
            name='url',
            field=models.URLField(default=api.models.url_default),
        ),
    ]