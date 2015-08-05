# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0017_delete_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='sat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sat1', models.IntegerField(default=0)),
                ('num1', models.IntegerField(default=0)),
                ('sat2', models.IntegerField(default=0)),
                ('num2', models.IntegerField(default=0)),
                ('sat3', models.IntegerField(default=0)),
                ('num3', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='citydata',
            name='smoney',
        ),
    ]
