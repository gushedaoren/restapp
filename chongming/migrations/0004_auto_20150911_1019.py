# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0003_auto_20150910_2107'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Nongjiale',
        ),
        migrations.DeleteModel(
            name='Youji',
        ),
    ]
