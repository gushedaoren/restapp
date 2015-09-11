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
                ('lastEditTime', models.DateTimeField(auto_now=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('content', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=150)),
                ('newsSource', models.CharField(max_length=150)),
                ('newsTime', models.DateTimeField()),
            ],
            options={
                'verbose_name': '\u65b0\u95fb',
                'verbose_name_plural': '\u65b0\u95fb',
            },
        ),
        migrations.CreateModel(
            name='Nongjiale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastEditTime', models.DateTimeField(auto_now=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('content', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to=b'', blank=True)),
                ('img1', models.ImageField(upload_to=b'', blank=True)),
                ('img2', models.ImageField(upload_to=b'', blank=True)),
                ('img3', models.ImageField(upload_to=b'', blank=True)),
                ('img4', models.ImageField(upload_to=b'', blank=True)),
                ('img5', models.ImageField(upload_to=b'', blank=True)),
            ],
            options={
                'verbose_name': '\u519c\u5bb6\u4e50',
                'verbose_name_plural': '\u519c\u5bb6\u4e50',
            },
        ),
        migrations.CreateModel(
            name='Youji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastEditTime', models.DateTimeField(auto_now=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('content', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=150)),
                ('icon_url', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'verbose_name': '\u6e38\u8bb0',
                'verbose_name_plural': '\u6e38\u8bb0',
            },
        ),
    ]
