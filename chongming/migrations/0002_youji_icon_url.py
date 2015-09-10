# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youji',
            name='icon_url',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
