# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0018_auto_20150805_0637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sat',
            old_name='num1',
            new_name='nosat1',
        ),
        migrations.RenameField(
            model_name='sat',
            old_name='num2',
            new_name='nosat2',
        ),
        migrations.RenameField(
            model_name='sat',
            old_name='num3',
            new_name='nosat3',
        ),
    ]
