# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0002_auto_20160415_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_no', models.CharField(max_length=100)),
                ('from_location', models.CharField(max_length=40)),
                ('to_location', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=40, choices=[(b'Dispatched', b'Dispatched'), (b'Pending', b'Pending'), (b'Out of Delivery', b'Out of Delivery'), (b'Delivered', b'Delivered')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
