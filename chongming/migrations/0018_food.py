# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0017_auto_20150923_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastEditTime', models.DateTimeField(auto_now=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('content', tinymce.models.HTMLField()),
                ('summary', models.TextField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('icon_url', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'verbose_name': '\u5d07\u660e\u7f8e\u98df',
                'verbose_name_plural': '\u5d07\u660e\u7f8e\u98df',
            },
        ),
    ]
