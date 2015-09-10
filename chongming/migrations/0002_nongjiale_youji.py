# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('chongming', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nongjiale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=150)),
                ('created', models.DateTimeField()),
                ('lastEditTime', models.DateTimeField()),
                ('content', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to=b'')),
                ('img1', models.ImageField(upload_to=b'')),
                ('img2', models.ImageField(upload_to=b'')),
                ('img3', models.ImageField(upload_to=b'')),
                ('img4', models.ImageField(upload_to=b'')),
                ('img5', models.ImageField(upload_to=b'')),
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
                ('title', models.CharField(unique=True, max_length=150)),
                ('created', models.DateTimeField()),
                ('lastEditTime', models.DateTimeField()),
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
