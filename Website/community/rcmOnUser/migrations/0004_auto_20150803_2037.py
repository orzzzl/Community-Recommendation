# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnUser', '0003_auto_20150803_2015'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='money',
            new_name='price',
        ),
    ]
