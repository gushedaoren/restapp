# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0008_auto_20150916_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='link',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
