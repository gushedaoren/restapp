# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0002_auto_20150911_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='nongjiale',
            name='busRoutes',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='nongjiale',
            name='carRoutes',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
