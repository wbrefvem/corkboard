# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cascade', '0002_auto_20150209_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialevent',
            old_name='on_bus_route',
            new_name='bus_impact',
        ),
        migrations.RenameField(
            model_name='specialevent',
            old_name='large_tents',
            new_name='large_tents_or_inflatables',
        ),
        migrations.RenameField(
            model_name='specialevent',
            old_name='pyro',
            new_name='open_flames',
        ),
        migrations.AddField(
            model_name='specialevent',
            name='emergency_action_plan',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specialevent',
            name='name',
            field=models.TextField(default='Your name here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialevent',
            name='set_up_time',
            field=models.TimeField(default=datetime.datetime(2015, 4, 16, 18, 33, 41, 778031, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialevent',
            name='status',
            field=models.CharField(default=None, max_length=2, choices=[(b'SU', b'Submitted'), (b'CO', b'Conditionally'), (b'PE', b'Permitted'), (b'PR', b'Problem')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specialevent',
            name='tear_down_time',
            field=models.TimeField(default=datetime.datetime(2015, 4, 16, 18, 33, 48, 32542, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialevent',
            name='trash_remove_plan',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
