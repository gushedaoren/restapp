# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0003_auto_20150911_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nongjiale',
            name='busRoutes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='carRoutes',
            field=models.TextField(),
        ),
    ]
