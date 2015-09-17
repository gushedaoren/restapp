# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0010_auto_20150917_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nongjiale',
            name='summary',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='youji',
            name='summary',
            field=models.TextField(max_length=150),
        ),
    ]
