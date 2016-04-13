# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0004_auto_20150731_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='scheduled_with',
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 10, 52, 983585, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 10, 52, 983681, tzinfo=utc), null=True, blank=True),
        ),
    ]
