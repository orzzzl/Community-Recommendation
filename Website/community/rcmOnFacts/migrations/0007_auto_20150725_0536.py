# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0006_auto_20150725_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='buy',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='rent',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
