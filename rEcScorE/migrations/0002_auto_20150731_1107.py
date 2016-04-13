# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='scheduled_with',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 7, 56, 600650, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 7, 56, 600740, tzinfo=utc), null=True, blank=True),
        ),
    ]
