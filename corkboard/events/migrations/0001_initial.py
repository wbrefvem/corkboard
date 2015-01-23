# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import oauth2client.django_orm
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('first_line', models.TextField()),
                ('second_line', models.TextField(null=True, blank=True)),
                ('city', models.TextField()),
                ('state', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AltDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('alt_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('cell', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('address', models.ForeignKey(to='events.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('credential', oauth2client.django_orm.CredentialsField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('org_type', models.CharField(choices=[('FP', 'For Profit'), ('NFP', 'Not for Profit')], max_length=2, default=None)),
                ('contact', models.ManyToManyField(to='events.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParticipantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecialEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('location', models.TextField()),
                ('date_submitted', models.DateField()),
                ('website', models.TextField()),
                ('purpose', models.TextField()),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('annual_event', models.BooleanField(default=False)),
                ('estimated_attendance', models.IntegerField()),
                ('previous_attendance', models.IntegerField(null=True, blank=True)),
                ('alcohol', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('large_tents', models.BooleanField(default=False)),
                ('on_bus_route', models.BooleanField(default=False)),
                ('amplified_music', models.BooleanField(default=False)),
                ('pyro', models.BooleanField(default=False)),
                ('hold_harmless_agree', models.BooleanField(default=False)),
                ('se_notif_reqs_agree', models.BooleanField(default=False)),
                ('legal_agree', models.BooleanField(default=False)),
                ('app_fee_agree', models.BooleanField(default=False)),
                ('alternative_dates', models.ManyToManyField(to='events.AltDate')),
                ('areas', models.ManyToManyField(to='events.Area')),
                ('beneficiary', models.ManyToManyField(to='events.Beneficiary')),
                ('event_day_contact', models.ForeignKey(to='events.Contact')),
                ('event_types', models.ManyToManyField(to='events.EventType')),
                ('organization', models.ManyToManyField(to='events.Organization')),
                ('participant_types', models.ManyToManyField(to='events.ParticipantType')),
                ('previous_events', models.ManyToManyField(to='events.SpecialEvent', related_name='previous_events_rel_+')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
