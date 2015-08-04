# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0011_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydata',
            name='money',
            field=models.IntegerField(default=b'0'),
        ),
    ]
