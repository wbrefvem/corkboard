from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from oauth2client.django_orm import CredentialsField
from phonenumber_field.modelfields import PhoneNumberField


class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    credential = CredentialsField()


class Address(models.Model):
    first_line = models.TextField()
    second_line = models.TextField(null=True, blank=True)
    city = models.TextField()
    state = models.TextField()
    zip_code = models.IntegerField(default=27601)


class Contact(models.Model):
    name = models.TextField()
    telephone = PhoneNumberField()
    cell = PhoneNumberField()
    address = models.ForeignKey(Address)
    email = models.TextField()


class Organization(models.Model):
    FOR_PROFIT = 'FP'
    NOT_FOR_PROFIT = 'NFP'
    ORG_TYPE_CHOICES = (
        (FOR_PROFIT, 'For Profit'),
        (NOT_FOR_PROFIT, 'Not for Profit')
    )
    name = models.CharField(max_length=256)
    address = models.ForeignKey(Address)
    org_type = models.CharField(max_length=2, choices=ORG_TYPE_CHOICES, default=None)
    contact = models.ManyToManyField(Contact)


class Beneficiary(models.Model):
    name = models.CharField(max_length=256)


class EventType(models.Model):
    text = models.TextField()


class ParticipantType(models.Model):
    text = models.TextField()


class AltDate(models.Model):
    alt_date = models.DateTimeField()


class Area(models.Model):
    name = models.TextField()


class Route(models.Model):
    text = models.TextField()


class SpecialEvent(models.Model):

    STATUSES = (
        ('SU', 'Submitted'),
        ('CO', 'Conditionally'),
        ('PE', 'Permitted'),
        ('PR', 'Problem')
    )

    name = models.TextField()
    location = models.TextField()
    route = models.OneToOneField(Route)
    organizations = models.ManyToManyField(Organization)
    date_submitted = models.DateField()
    website = models.TextField()
    purpose = models.TextField()
    beneficiaries = models.ManyToManyField(Beneficiary)

    date = models.DateField()
    alternative_dates = models.ManyToManyField(AltDate)
    start_time = models.TimeField()
    end_time = models.TimeField()
    set_up_time = models.TimeField()
    tear_down_time = models.TimeField()

    event_types = models.ManyToManyField(EventType)
    participant_types = models.ManyToManyField(ParticipantType)
    annual_event = models.BooleanField(default=False)
    estimated_attendance = models.IntegerField()
    previous_attendance = models.IntegerField(null=True, blank=True)
    previous_events = models.ManyToManyField("self")

    trash_removal_plan = models.TextField(null=True)
    emergency_action_plan = models.TextField(null=True)

    areas = models.ManyToManyField(Area)
    alcohol = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    large_tents_or_inflatables = models.BooleanField(default=False)
    bus_impact = models.BooleanField(default=False)
    amplified_music = models.BooleanField(default=False)
    open_flames = models.BooleanField(default=False)
    closures = models.CharField(max_length=256)

    hold_harmless_agree = models.BooleanField(default=False)
    se_notif_reqs_agree = models.BooleanField(default=False)
    legal_agree = models.BooleanField(default=False)
    app_fee_agree = models.BooleanField(default=False)

    status = models.CharField(max_length=2, choices=STATUSES, default=None)

admin.site.register(SpecialEvent)
admin.site.register(Area)
admin.site.register(AltDate)
admin.site.register(ParticipantType)
admin.site.register(EventType)
admin.site.register(Beneficiary)
admin.site.register(Organization)
admin.site.register(Contact)
admin.site.register(Address)
