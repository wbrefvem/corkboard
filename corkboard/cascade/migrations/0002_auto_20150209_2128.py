# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cascade', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.TextField(default='default name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.ForeignKey(default=-1, to='cascade.Address'),
            preserve_default=False,
        ),
    ]
