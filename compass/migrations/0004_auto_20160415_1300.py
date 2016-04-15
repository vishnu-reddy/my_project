# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0003_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
