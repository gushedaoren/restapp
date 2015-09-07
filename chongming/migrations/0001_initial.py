# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('created', models.DateTimeField()),
                ('lastEditTime', models.DateTimeField()),
                ('content', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=150)),
                ('newsSource', models.CharField(max_length=150)),
                ('newsTime', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
