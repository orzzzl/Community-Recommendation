# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0004_auto_20150719_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='americanIndian',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='asian',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='black',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='hawaiian',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='hispanic',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='otherRace',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='twoOrMore',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='white',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
