# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0005_auto_20150911_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='nongjiale',
            name='enable_comments',
            field=models.BooleanField(default=True),
        ),
    ]
