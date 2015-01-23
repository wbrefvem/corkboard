from django import forms
from events import models

FIELDS = [
    'location',
    'organization',
    'date_submitted',
    'website',
    'purpose',
    'beneficiary',
    'date',
    'alternative_dates',
    'event_day_contact',
    'start_time',
    'end_time',
    'event_types',
    'participant_types',
    'annual_event',
    'estimated_attendance',
    'previous_attendance',
    'previous_events',
    'areas',
    'alcohol',
    'food',
    'large_tents',
    'on_bus_route',
    'amplified_music',
    'pyro',
    'hold_harmless_agree',
    'se_notif_reqs_agree',
    'legal_agree',
    'app_fee_agree'
]


class SpecialEventForm(forms.ModelForm):
    alcohol = forms.BooleanField(required=False)
    food = forms.BooleanField(required=False)
    large_tents = forms.BooleanField(required=False)
    on_bus_route = forms.BooleanField(required=False)
    amplified_music = forms.BooleanField(required=False)
    pyro = forms.BooleanField(required=False)

    organization = forms.CharField(max_length=256)
    beneficiary = forms.CharField(max_length=256)
    alternative_dates = forms.CharField(max_length=256)
    event_day_contact = forms.CharField(max_length=256)
    event_types = forms.CharField(max_length=256)
    participant_types = forms.CharField(max_length=256)
    previous_events = forms.CharField(max_length=256)
    areas = forms.CharField(max_length=256)

    class Meta:
        model = models.SpecialEvent
        fields = FIELDS




