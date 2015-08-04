# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0013_auto_20150803_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='smoney',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
