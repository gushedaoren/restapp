# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0009_auto_20150916_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='nongjiale',
            name='hot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nongjiale',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nongjiale',
            name='summary',
            field=models.TextField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='youji',
            name='hot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='youji',
            name='summary',
            field=models.TextField(max_length=150, blank=True),
        ),
    ]
