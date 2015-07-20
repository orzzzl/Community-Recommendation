# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='femalePercentage',
            field=models.FloatField(default=b'-1.0'),
        ),
    ]
