# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0003_auto_20150719_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citydata',
            name='divorced',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AlterField(
            model_name='citydata',
            name='femalePercentage',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AlterField(
            model_name='citydata',
            name='malePercentage',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AlterField(
            model_name='citydata',
            name='neverMarried',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AlterField(
            model_name='citydata',
            name='nowMarried',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AlterField(
            model_name='citydata',
            name='seperated',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AlterField(
            model_name='citydata',
            name='widowed',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
