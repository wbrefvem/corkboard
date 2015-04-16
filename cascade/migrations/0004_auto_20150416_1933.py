# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cascade', '0003_auto_20150416_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialevent',
            old_name='organization',
            new_name='organizations',
        ),
        migrations.AddField(
            model_name='specialevent',
            name='closures',
            field=models.CharField(default='None', max_length=256),
            preserve_default=False,
        ),
    ]
