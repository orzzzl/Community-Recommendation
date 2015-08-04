# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0012_citydata_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citydata',
            name='money',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
