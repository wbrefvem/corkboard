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
    class Meta:
        model = models.SpecialEvent
        fields = FIELDS


