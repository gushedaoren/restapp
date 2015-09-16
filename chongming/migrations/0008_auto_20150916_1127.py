# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0007_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nongjiale',
            name='busRoutes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='carRoutes',
            field=models.TextField(blank=True),
        ),
    ]
