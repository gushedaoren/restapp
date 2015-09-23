# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0015_auto_20150923_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shanghu',
            name='contact',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
