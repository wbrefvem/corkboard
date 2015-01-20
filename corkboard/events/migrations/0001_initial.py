# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oauth2client.django_orm
import phonenumber_field.modelfields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_line', models.TextField()),
                ('second_line', models.TextField(blank=True, null=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('alt_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('id', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credential', oauth2client.django_orm.CredentialsField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('org_type', models.CharField(default=None, max_length=2, choices=[('FP', 'For Profit'), ('NFP', 'Not for Profit')])),
                ('contact', models.ManyToManyField(to='events.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParticipantType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecialEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('location', models.TextField()),
                ('date_submitted', models.DateTimeField()),
                ('website', models.TextField()),
                ('purpose', models.TextField()),
                ('date', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('annual_event', models.BooleanField()),
                ('estimated_attendance', models.IntegerField()),
                ('previous_attendance', models.IntegerField(blank=True, null=True)),
                ('alcohol', models.BooleanField()),
                ('food', models.BooleanField()),
                ('large_tents', models.BooleanField()),
                ('on_bus_route', models.BooleanField()),
                ('amplified_music', models.BooleanField()),
                ('pyro', models.BooleanField()),
                ('hold_harmless_agree', models.BooleanField()),
                ('se_notif_reqs_agree', models.BooleanField()),
                ('legal_agree', models.BooleanField()),
                ('app_fee_agree', models.BooleanField()),
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
