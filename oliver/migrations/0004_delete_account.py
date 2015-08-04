# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oliver', '0003_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
