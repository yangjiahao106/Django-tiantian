# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0001_initial'),
        ('app_user', '0004_auto_20171222_1347'),
        ('app_cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('count', models.IntegerField()),
                ('gid', models.ForeignKey(to='app_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('onumber', models.CharField(max_length=20)),
                ('ototal', models.DecimalField(max_digits=6, decimal_places=2)),
                ('odate', models.DateField(auto_now=True)),
                ('oispay', models.BooleanField(default=False)),
                ('oaddress', models.CharField(max_length=150)),
                ('uid', models.ForeignKey(to='app_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='oid',
            field=models.ForeignKey(to='app_cart.OrderInfo'),
        ),
    ]
