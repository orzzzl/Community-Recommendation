# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0007_auto_20150725_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='bachelor',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='highSchool',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AddField(
            model_name='citydata',
            name='master',
            field=models.FloatField(default=b'0.0'),
        ),
    ]
