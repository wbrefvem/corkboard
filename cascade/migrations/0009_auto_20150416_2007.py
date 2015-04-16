# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cascade', '0008_remove_specialevent_event_day_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.ForeignKey(default=1, to='cascade.Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.TextField(default='me@you.com'),
            preserve_default=False,
        ),
    ]
