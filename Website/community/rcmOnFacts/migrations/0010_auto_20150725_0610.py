# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0009_citydata_noeducation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citydata',
            old_name='noeducation',
            new_name='noEducation',
        ),
    ]
