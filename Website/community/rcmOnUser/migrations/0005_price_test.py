# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnUser', '0004_auto_20150803_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='test',
            field=models.CharField(default=b'#####', max_length=10),
        ),
    ]
