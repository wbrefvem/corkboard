from django.db import models
from django.contrib.auth.models import User
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


class Contact(models.Model):
    user = models.ForeignKey(User)
    address = models.ForeignKey(Address)
    telephone = PhoneNumberField()
    cell = PhoneNumberField()


class Organization(models.Model):
    FOR_PROFIT = 'FP'
    NOT_FOR_PROFIT = 'NFP'
    ORG_TYPE_CHOICES = (
        (FOR_PROFIT, 'For Profit'),
        (NOT_FOR_PROFIT, 'Not for Profit')
    )
    name = models.CharField(max_length=256)
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


class SpecialEvent(models.Model):
    location = models.TextField()
    organization = models.ManyToManyField(Organization)
    date_submitted = models.DateTimeField()
    website = models.TextField()
    purpose = models.TextField()
    beneficiary = models.ManyToManyField(Beneficiary)

    date = models.DateTimeField()
    alternative_dates = models.ManyToManyField(AltDate)
    event_day_contact = models.ForeignKey(Contact)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    event_types = models.ManyToManyField(EventType)
    participant_types = models.ManyToManyField(ParticipantType)
    annual_event = models.BooleanField()
    estimated_attendance = models.IntegerField()
    previous_attendance = models.IntegerField(null=True, blank=True)
    previous_events = models.ManyToManyField("self")

    areas = models.ManyToManyField(Area)
    alcohol = models.BooleanField()
    food = models.BooleanField()
    large_tents = models.BooleanField()
    on_bus_route = models.BooleanField()
    amplified_music = models.BooleanField()
    pyro = models.BooleanField()

    hold_harmless_agree = models.BooleanField()
    se_notif_reqs_agree = models.BooleanField()
    legal_agree = models.BooleanField()
    app_fee_agree = models.BooleanField()
