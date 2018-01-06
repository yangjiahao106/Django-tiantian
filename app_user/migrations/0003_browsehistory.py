# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0001_initial'),
        ('app_user', '0002_auto_20171221_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.ForeignKey(to='app_goods.GoodsInfo')),
                ('uid', models.ForeignKey(to='app_user.UserInfo')),
            ],
        ),
    ]
