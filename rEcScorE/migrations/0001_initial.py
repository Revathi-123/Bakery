# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidate_name', models.CharField(default=None, max_length=100)),
                ('job_title', models.CharField(default=None, max_length=100)),
                ('experience', models.CharField(default=None, max_length=2)),
                ('highest_degree', models.CharField(default=None, max_length=100)),
                ('city', models.CharField(default=None, max_length=50)),
                ('country', models.CharField(default=None, max_length=50)),
                ('source', models.CharField(default=None, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(default=None, max_length=50)),
                ('screening_score_1', models.CharField(default=None, max_length=2)),
                ('status_1', models.CharField(max_length=3, choices=[(b'R', b'Rejected'), (b'S', b'Scheduled'), (b'H', b'Hired')])),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('your_name', models.CharField(default=None, max_length=100)),
                ('dob', models.DateTimeField(default=datetime.datetime(2015, 7, 31, 10, 46, 9, 950629, tzinfo=utc), null=True, blank=True)),
                ('city', models.CharField(default=None, max_length=50)),
                ('country', models.CharField(default=None, max_length=50)),
                ('highest_degree', models.CharField(default=None, max_length=100)),
                ('doj', models.DateTimeField(default=datetime.datetime(2015, 7, 31, 10, 46, 9, 950793, tzinfo=utc), null=True, blank=True)),
                ('designation', models.CharField(default=None, max_length=100)),
                ('Profile_Pic', models.ImageField(null=True, upload_to=b'img/documents/', blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date(2015, 7, 31))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
    ]
