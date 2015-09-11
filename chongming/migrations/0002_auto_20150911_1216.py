# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nongjiale',
            old_name='author',
            new_name='contact',
        ),
        migrations.AddField(
            model_name='nongjiale',
            name='address',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nongjiale',
            name='phone',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
