# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cascade', '0007_auto_20150416_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialevent',
            name='event_day_contact',
        ),
    ]
