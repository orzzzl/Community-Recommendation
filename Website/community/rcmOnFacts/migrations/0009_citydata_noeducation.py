# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0008_auto_20150725_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='noeducation',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
