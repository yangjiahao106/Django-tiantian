# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_auto_20171222_1347'),
        ('app_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('gnumber', models.IntegerField(default=1)),
                ('gid', models.ForeignKey(to='app_goods.GoodsInfo')),
                ('uid', models.ForeignKey(to='app_user.UserInfo')),
            ],
        ),
    ]
