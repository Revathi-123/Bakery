# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0007_auto_20150731_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 3, 37, 10, 839909, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 3, 37, 10, 840344, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 11, 12)),
        ),
    ]
