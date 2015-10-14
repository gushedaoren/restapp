# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
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
                ('index', models.IntegerField(default=0)),
                ('logo', models.ImageField(upload_to=b'', blank=True)),
                ('img1', models.ImageField(upload_to=b'', blank=True)),
                ('img2', models.ImageField(upload_to=b'', blank=True)),
                ('img3', models.ImageField(upload_to=b'', blank=True)),
                ('img4', models.ImageField(upload_to=b'', blank=True)),
                ('img5', models.ImageField(upload_to=b'', blank=True)),
                ('link', models.CharField(max_length=150, blank=True)),
            ],
            options={
                'verbose_name': '\u5e7f\u544a',
                'verbose_name_plural': '\u5e7f\u544a',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastEditTime', models.DateTimeField(auto_now=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('content', tinymce.models.HTMLField()),
                ('summary', models.TextField(max_length=150)),
                ('author', models.CharField(default=b'\xe4\xbd\x9a\xe5\x90\x8d', max_length=150)),
                ('icon_url', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'verbose_name': '\u7f8e\u98df',
                'verbose_name_plural': '\u7f8e\u98df',
            },
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastEditTime', models.DateTimeField(auto_now=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('content', tinymce.models.HTMLField()),
                ('summary', models.TextField(max_length=150)),
                ('author', models.CharField(default=b'\xe4\xbd\x9a\xe5\x90\x8d', max_length=150)),
                ('source', models.CharField(max_length=150)),
                ('icon_url', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'verbose_name': '\u5065\u5eb7',
                'verbose_name_plural': '\u5065\u5eb7',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastEditTime', models.DateTimeField(auto_now=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('content', tinymce.models.HTMLField()),
                ('summary', models.TextField(max_length=150)),
                ('author', models.CharField(default=b'\xe4\xbd\x9a\xe5\x90\x8d', max_length=150)),
                ('newsSource', models.CharField(max_length=150)),
                ('newsTime', models.DateTimeField()),
                ('icon_url', models.CharField(max_length=1000, blank=True)),
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
                ('summary', models.TextField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('busRoutes', models.TextField(blank=True)),
                ('carRoutes', models.TextField(blank=True)),
                ('hot', models.IntegerField(default=0, verbose_name=b'\xe7\x83\xad\xe9\x97\xa8')),
                ('rank', models.IntegerField(default=0, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90')),
                ('logo', models.ImageField(upload_to=b'', blank=True)),
                ('img1', models.ImageField(upload_to=b'', blank=True)),
                ('img2', models.ImageField(upload_to=b'', blank=True)),
                ('img3', models.ImageField(upload_to=b'', blank=True)),
                ('img4', models.ImageField(upload_to=b'', blank=True)),
                ('img5', models.ImageField(upload_to=b'', blank=True)),
                ('enable_comments', models.BooleanField(default=True)),
                ('njlShow', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'verbose_name': '\u519c\u5bb6\u4e50',
                'verbose_name_plural': '\u519c\u5bb6\u4e50',
            },
        ),
        migrations.CreateModel(
            name='Shanghu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('contact', models.CharField(max_length=150, blank=True)),
                ('phone', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250, blank=True)),
                ('remark', tinymce.models.HTMLField(blank=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '\u5546\u6237\u901a\u8baf\u5f55',
                'verbose_name_plural': '\u5546\u6237\u901a\u8baf\u5f55',
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
                ('summary', models.TextField(max_length=150)),
                ('hot', models.IntegerField(default=0)),
                ('author', models.CharField(default=b'\xe4\xbd\x9a\xe5\x90\x8d', max_length=150)),
                ('icon_url', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'verbose_name': '\u6e38\u8bb0',
                'verbose_name_plural': '\u6e38\u8bb0',
            },
        ),
    ]
