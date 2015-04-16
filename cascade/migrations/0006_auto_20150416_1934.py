# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cascade', '0005_auto_20150416_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialevent',
            old_name='beneficiary',
            new_name='beneficiaries',
        ),
    ]
