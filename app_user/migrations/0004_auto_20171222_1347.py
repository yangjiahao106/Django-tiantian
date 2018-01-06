# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_browsehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='rcode',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='recipient',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='rphone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
