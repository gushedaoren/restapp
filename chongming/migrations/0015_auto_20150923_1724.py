# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0014_auto_20150923_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shanghu',
            name='address',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='shanghu',
            name='remark',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
