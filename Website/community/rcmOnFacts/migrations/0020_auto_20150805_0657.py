# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0019_auto_20150805_0641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sat',
            name='nosat1',
        ),
        migrations.RemoveField(
            model_name='sat',
            name='nosat2',
        ),
        migrations.RemoveField(
            model_name='sat',
            name='nosat3',
        ),
        migrations.RemoveField(
            model_name='sat',
            name='sat1',
        ),
        migrations.RemoveField(
            model_name='sat',
            name='sat2',
        ),
        migrations.RemoveField(
            model_name='sat',
            name='sat3',
        ),
        migrations.AddField(
            model_name='sat',
            name='nosat',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sat',
            name='sat',
            field=models.IntegerField(default=1),
        ),
    ]
