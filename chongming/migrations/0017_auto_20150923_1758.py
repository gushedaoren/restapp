# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0016_auto_20150923_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shanghu',
            name='title',
            field=models.CharField(unique=True, max_length=150),
        ),
    ]
