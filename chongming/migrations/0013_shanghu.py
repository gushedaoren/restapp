# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0012_auto_20150920_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shanghu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('remark', tinymce.models.HTMLField()),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '\u5546\u6237\u901a\u8baf\u5f55',
                'verbose_name_plural': '\u5546\u6237\u901a\u8baf\u5f55',
            },
        ),
    ]
