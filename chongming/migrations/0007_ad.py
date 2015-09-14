# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0006_nongjiale_enable_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='AD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastEditTime', models.DateTimeField(auto_now=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('content', tinymce.models.HTMLField()),
                ('logo', models.ImageField(upload_to=b'', blank=True)),
                ('img1', models.ImageField(upload_to=b'', blank=True)),
                ('img2', models.ImageField(upload_to=b'', blank=True)),
                ('img3', models.ImageField(upload_to=b'', blank=True)),
                ('img4', models.ImageField(upload_to=b'', blank=True)),
                ('img5', models.ImageField(upload_to=b'', blank=True)),
                ('link', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': '\u5e7f\u544a',
                'verbose_name_plural': '\u5e7f\u544a',
            },
        ),
    ]
