# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnUser', '0005_price_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipCode', models.CharField(default=b'#####', max_length=10)),
                ('money', models.IntegerField(default=b'0')),
                ('school', models.FloatField(default=b'0.0')),
                ('eating', models.FloatField(default=b'0.0')),
                ('shopping', models.FloatField(default=b'0.0')),
                ('security', models.FloatField(default=b'0.0')),
                ('health', models.FloatField(default=b'0.0')),
                ('transportation', models.FloatField(default=b'0.0')),
                ('clinicNumber', models.IntegerField(default=b'0')),
                ('preschoolNumber', models.IntegerField(default=b'0')),
            ],
        ),
        migrations.DeleteModel(
            name='price',
        ),
    ]
