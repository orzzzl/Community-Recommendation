# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0015_delete_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipCode', models.CharField(default=b'#####', max_length=10)),
                ('money', models.IntegerField(default=b'0')),
            ],
        ),
    ]
