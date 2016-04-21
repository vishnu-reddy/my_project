# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0002_auto_20160418_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='email',
            field=models.EmailField(max_length=50),
            preserve_default=True,
        ),
    ]
