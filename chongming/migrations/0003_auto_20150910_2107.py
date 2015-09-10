# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0002_nongjiale_youji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nongjiale',
            name='img1',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='img2',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='img3',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='img4',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='img5',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='logo',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
