from django import forms
from cascade import models

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


class ContactMultipleChoiceField(forms.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return "%s, %s" % (obj.user.last_name, obj.user.first_name)


class OrganizationForm(forms.ModelForm):
    contact = ContactMultipleChoiceField(queryset=models.Contact.objects.all())

    class Meta:
        model = models.Organization
        fields = '__all__'


class CustomBooleanField(forms.BooleanField):
    pass

class BlobForm(forms.Form):

    COMPETITOR = 'CM'
    RR_OUTFITTERS = 'OC'
    SAINT_PATS = 'SP'

    ORGANIZATION_CHOICES = (
        (COMPETITOR, 'Competitor Group, Inc.'),
        (RR_OUTFITTERS, 'Raleigh Running Outfitters'),
        (SAINT_PATS, "St. Patrick's Day Committee")
    )

    TOYS_FOR_TOTS = 'TT'
    SALVATION_ARMY = 'SA'

    BENEFICIARY_CHOICES = (
        (TOYS_FOR_TOTS, 'Toys for Tots'),
        (SALVATION_ARMY, 'Salvation Army')
    )

    ROCK_AND_ROLL = 'RR'
    OAK_CITY = 'OC'
    PREVIOUS_EVENTS_CHOICES = (
        (ROCK_AND_ROLL, 'Rock & Roll Marathon 2014'),
        (OAK_CITY, 'Oak City Marthon 2014'),
        (SAINT_PATS, "Saint Patrick's Day Parade 2014")
    )

    FIVE_K = '5K'
    EIGHT_K = '8K'
    TEN_K = '10'
    WALK = 'WA'
    MARATHON = 'MA'
    HALF_MARATHON = 'HM'
    BIKE_RACE = 'BR'
    PARADE = 'PA'
    TRIATHLON = 'TR'
    ONE_MILE = '1M'
    OTHER = 'OT'

    EVENT_TYPE_CHOICES = (
        (FIVE_K, '5k'),
        (EIGHT_K, '8k'),
        (TEN_K, '10k'),
        (WALK, 'Walk'),
        (MARATHON, 'Marathon'),
        (HALF_MARATHON, 'Half Marathon'),
        (BIKE_RACE, 'Bike Race'),
        (PARADE, 'Parade'),
        (TRIATHLON, 'Triathlon'),
        (ONE_MILE, '1 Mile'),
        (OTHER, 'Other')
    )

    PARTICIPANTS = 'PR'
    SPECTATORS = 'SP'
    ANIMALS = 'AN'
    VEHICLES = 'VE'
    BIKES = 'BI'
    FLOATS = 'FL'
    BANDS = 'BA'
    FOOD_VENDORS = 'FV'
    MERCHANDISE_VENDORS = 'MV'

    PARTICIPANT_TYPE_CHOICES = (
        (PARTICIPANTS, 'Participants'),
        (SPECTATORS, 'Spectators'),
        (ANIMALS, 'Animals'),
        (VEHICLES, 'Vehicles'),
        (BIKES, 'Bikes'),
        (FLOATS, 'FL'),
        (BANDS, 'Bands'),
        (FOOD_VENDORS, 'FV'),
        (MERCHANDISE_VENDORS, 'Merchandise Vendors'),
        (OTHER, 'Other')
    )

    CITY_PLAZA = 'CP'
    CITY_PLAZA_ASTROTURF = 'CA'
    MOORE_SQUARE = 'MS'
    NASH_SQUARE = 'NS'
    OTHER_DOWNTOWN = 'OD'
    HILLSBOROUGH = 'HB'
    CAMERON_VILLAGE_PARK = 'CV'
    BRIER_CREEK = 'BC'
    NORTH_HILLS = 'NH'
    BOYLAN_HEIGHTS = 'BH'
    OAKWOOD_MORDECAI = 'OM'
    WAKEFIELD = 'WF'
    CITY_GREENWAYS = 'CG'
    NONE = 'NO'

    SPECIAL_ZONE_CHOICES = (
        (CITY_PLAZA, 'City Plaza'),
        (CITY_PLAZA_ASTROTURF, 'City Plaza Astroturf'),
        (MOORE_SQUARE, 'Moore Square'),
        (NASH_SQUARE, 'Nash Square'),
        (OTHER_DOWNTOWN, 'Other Downtown Locations'),
        (HILLSBOROUGH, 'Hillsborough Street'),
        (CAMERON_VILLAGE_PARK, 'Cameron Village / Cameron Park Area'),
        (BRIER_CREEK, 'Brier Creek'),
        (NORTH_HILLS, 'North Hills'),
        (BOYLAN_HEIGHTS, 'Boylan Heights'),
        (OAKWOOD_MORDECAI, 'Oakwood / Mordecai'),
        (WAKEFIELD, 'Wakefield'),
        (CITY_GREENWAYS, 'City Greenways'),
        (NONE, 'None of the above'),
    )

    location = forms.CharField()
    organization = forms.ChoiceField(choices=ORGANIZATION_CHOICES)
    date_submitted = forms.DateTimeField()
    website = forms.CharField()
    purpose = forms.CharField()
    beneficiary = forms.ChoiceField(choices=BENEFICIARY_CHOICES)

    date = forms.DateTimeField()
    alternative_dates = forms.DateTimeField()
    event_day_contact = forms.CharField()
    start_time = forms.CharField()
    end_time = forms.CharField()
    route_description = forms.CharField()
    route_map = forms.FileField()
    route_url = forms.URLField()
    comments = forms.CharField()

    event_types = forms.MultipleChoiceField(choices=EVENT_TYPE_CHOICES)
    participant_types = forms.MultipleChoiceField(choices=PARTICIPANT_TYPE_CHOICES)
    estimated_attendance = forms.IntegerField()
    previous_attendance = forms.IntegerField(required=False)
    previous_events = forms.ChoiceField(choices=PREVIOUS_EVENTS_CHOICES)

    trash_removal_plan = forms.CharField()
    updated_trash_removal_plan = forms.FileField()
    emergency_action_plan = forms.CharField()

    special_event_zones = forms.MultipleChoiceField()
    annual_event = CustomBooleanField(label="This is an annual event.")
    alcohol = CustomBooleanField(label="There will be alcoholic beverages at this event.")
    food = CustomBooleanField(label="The event will sell food.")
    large_tents = CustomBooleanField(label="There will be tents or inflatable structures in excess of 400 square feet.")
    bus_route_impact = CustomBooleanField(label="This event impacts CAT or TTA bus routes.")
    amplified_music = CustomBooleanField(label="There will be amplified music.")
    pyro = CustomBooleanField(label="The event will involve fireworks, pyrotechnics or other open flame.")

    hold_harmless_agree = CustomBooleanField()
    se_notif_reqs_agree = CustomBooleanField()
    legal_agree = CustomBooleanField()
    app_fee_agree = CustomBooleanField()
