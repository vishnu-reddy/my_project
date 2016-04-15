# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.IntegerField()),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='country',
            field=models.CharField(max_length=40, choices=[(b'UAE', b'UAE'), (b'Saudi Arabic', b'Saudi Arabic'), (b'Oman', b'Oman'), (b'Qatar', b'Qatar'), (b'Bahrain', b'Bahrain')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
