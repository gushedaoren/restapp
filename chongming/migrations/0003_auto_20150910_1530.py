# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0002_youji_icon_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youji',
            name='icon_url',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
