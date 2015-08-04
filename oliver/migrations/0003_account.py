# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oliver', '0002_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accountName', models.CharField(max_length=200, unique=True, null=True)),
                ('password', models.CharField(max_length=200)),
                ('nick', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10, choices=[(b'm', b'Man'), (b'w', b'Woman')])),
            ],
        ),
    ]
