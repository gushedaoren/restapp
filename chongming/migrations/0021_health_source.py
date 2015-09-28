# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0020_auto_20150928_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='source',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
