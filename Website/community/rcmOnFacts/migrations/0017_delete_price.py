# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0016_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
    ]
