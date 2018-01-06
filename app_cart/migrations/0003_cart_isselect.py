# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0002_auto_20171225_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='isselect',
            field=models.BooleanField(default=True),
        ),
    ]
