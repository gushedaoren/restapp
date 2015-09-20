# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0011_auto_20150917_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nongjiale',
            name='njlShow',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='hot',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x83\xad\xe9\x97\xa8'),
        ),
        migrations.AlterField(
            model_name='nongjiale',
            name='rank',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90'),
        ),
    ]
