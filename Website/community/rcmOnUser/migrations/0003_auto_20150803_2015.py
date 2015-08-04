# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnUser', '0002_auto_20150803_2012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='price',
            new_name='money',
        ),
    ]
