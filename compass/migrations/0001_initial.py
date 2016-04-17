# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currernt_date', models.DateField()),
                ('current_from_location', models.CharField(max_length=100)),
                ('current_to_location', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=40, choices=[(b'Dispatched', b'Dispatched'), (b'Pending', b'Pending'), (b'Out of Delivery', b'Out of Delivery'), (b'Delivered', b'Delivered')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
                ('country', models.CharField(max_length=40, choices=[(b'UAE', b'UAE'), (b'Saudi Arabic', b'Saudi Arabic'), (b'Oman', b'Oman'), (b'Qatar', b'Qatar'), (b'Bahrain', b'Bahrain')])),
                ('enquiry', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, null=True, blank=True)),
                ('email', models.CharField(max_length=40, null=True, blank=True)),
                ('phone', models.IntegerField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_no', models.CharField(max_length=100)),
                ('from_location', models.CharField(max_length=40)),
                ('to_location', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=40, choices=[(b'Dispatched', b'Dispatched'), (b'Pending', b'Pending'), (b'Out of Delivery', b'Out of Delivery'), (b'Delivered', b'Delivered')])),
                ('no_of_pieces', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='currentstatus',
            name='reference_no',
            field=models.ForeignKey(to='compass.Track'),
            preserve_default=True,
        ),
    ]
