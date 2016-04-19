# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='country',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='services',
            field=models.CharField(max_length=40, choices=[(b'Vessel Agency', b'Vessel Agency'), (b'Customs Clearance', b'Customs Clearance'), (b'Transportation', b'Transportation'), (b'Freight Forwarding', b'Freight Forwarding'), (b'Ship Chandling', b'Ship Chandling'), (b'P & I Correspondents', b'P & I Correspondents')]),
            preserve_default=True,
        ),
    ]
