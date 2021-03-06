# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0002_auto_20150731_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='scheduled_with',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 8, 34, 418730, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 8, 34, 418866, tzinfo=utc), null=True, blank=True),
        ),
    ]
