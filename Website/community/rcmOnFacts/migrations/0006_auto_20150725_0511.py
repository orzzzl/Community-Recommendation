# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0005_auto_20150720_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='gay',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='lesbian',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
