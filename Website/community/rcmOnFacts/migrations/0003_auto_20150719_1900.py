# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0002_citydata_femalepercentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='divorced',
            field=models.FloatField(default=b'-1.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='neverMarried',
            field=models.FloatField(default=b'-1.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='nowMarried',
            field=models.FloatField(default=b'-1.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='seperated',
            field=models.FloatField(default=b'-1.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='widowed',
            field=models.FloatField(default=b'-1.0'),
        ),
    ]
