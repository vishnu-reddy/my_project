# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('services', models.CharField(max_length=40, choices=[(b'Land Freight Management', b'Land Freight Management'), (b'Sea Freight Management', b'Sea Freight Management'), (b'Air Freight Management', b'Air Freight Management'), (b'Customs Clearance', b'Customs Clearance'), (b'Worldwide Door Delivery', b'Worldwide Door Delivery'), (b'Project Cargo Handling', b'Project Cargo Handling'), (b'Marine Insurance', b'Marine Insurance')])),
                ('full_name', models.CharField(max_length=30)),
                ('organisation', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
                ('contact_number', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=40, choices=[(b'USA', b'USA'), (b'Saudi Arabia', b'Saudi Arabia'), (b'Oman', b'Oman'), (b'Qatar', b'Qatar'), (b'Bahrain', b'Bahrain')])),
                ('enquiry', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
