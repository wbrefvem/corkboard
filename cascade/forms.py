from django import forms
from cascade import models
from django.conf import settings

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


class SpecialEventForm(forms.ModelForm):
    class Meta:
        model = models.SpecialEvent


class BlobForm(forms.Form):

    COMPETITOR = 'CM'
    RR_OUTFITTERS = 'OC'
    SAINT_PATS = 'SP'

    ORGANIZATION_CHOICES = (
        ('Competitor Group, Inc.', 'Competitor Group, Inc.'),
        ('Raleigh Running Outfitters', 'Raleigh Running Outfitters'),
        ("St. Patrick's Day Committee", "St. Patrick's Day Committee")
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

    RUN = 'RU'
    BIKE = 'BI'

    EVENT_TYPE_CHOICES = (
        ("Parade", "Parade"),
        ("Run", "Run"),
        ("Bike", "Bike")    
    )
    
    # EVENT_TYPE_CHOICES = (
    #     (FIVE_K, '5k'),
    #     (EIGHT_K, '8k'),
    #     (TEN_K, '10k'),
    #     (WALK, 'Walk'),
    #     (MARATHON, 'Marathon'),
    #     (HALF_MARATHON, 'Half Marathon'),
    #     (BIKE_RACE, 'Bike Race'),
    #     (PARADE, 'Parade'),
    #     (TRIATHLON, 'Triathlon'),
    #     (ONE_MILE, '1 Mile'),
    #     (OTHER, 'Other')
    # )

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

    CITY_PLAZA = 'City Plaza'
    CITY_PLAZA_ASTROTURF = 'City Plaza AstroTurf'
    MOORE_SQUARE = 'Moore Square'
    NASH_SQUARE = 'Nash Square'
    OTHER_DOWNTOWN = 'Other Downtown Locations'
    HILLSBOROUGH = 'Hillsborough'
    CAMERON_VILLAGE_PARK = 'Cameron Village/Cameron Park'
    BRIER_CREEK = 'Brier Creek'
    NORTH_HILLS = 'North Hill'
    BOYLAN_HEIGHTS = 'Boylan Heights'
    OAKWOOD_MORDECAI = 'Oakwood/Mordecai'
    WAKEFIELD = 'Wakefield'
    CITY_GREENWAYS = 'City Greenways'
    NONE = 'None of the above'

    SPECIAL_ZONE_CHOICES = (
        (CITY_PLAZA, 'City Plaza'),
        (CITY_PLAZA_ASTROTURF, 'City Plaza AstroTurf'),
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

    HOLD_HARMLESS_TEXT = "I have read the hold harmless agreement and liability agreement. \
                      I agree to maintain public liability and property damage insurance \
                      if the Revenue Bureau determines a liability agreement will be required, \
                      per Street and Sidewalk Use Administrative Regulations, section 10.B."

    SE_NOTIF_REQS_AGREE_TEXT = "I have read and understand the Special Event Notification Requirements and agree to abide by these city policies."

    LEGAL_AGREE_TEXT = "I agree to conform to all city, state, and federal laws and regulations.  \
                        I accept responsibility for the removal of trash, paper, etc. from and \
                        general cleaning of the premises.  In the event that the site area is not \
                        cleaned after use, the cleanup fee may be taken out of the deposit or the \
                        applicant will be billed for additional clean-up by the City of Raleigh.  \
                        I agree to be accountable for any damage to the event site.  I understand \
                        that all necessary fees, insurance, outside permits, etc. must be submitted \
                        with the application before the issuance of the event permit."

    APP_FEE_AGREE_TEXT = "I understand that I am required to pay the corresponding nonrefundable \
                          application fee for this event before the submission deadline, and that \
                          my application will not be reviewed until this payment has been received."

    ARC_GIS_FIELDS = [
        'EVENT_NAME',
        'LOCATION',
        'PRODUCTION_ORG',
        'CONTACT_NAME',
        'CONTACT_PHONE',
        'CONTACT_EMAIL',
        'CONTACT_ADDRESS',
        'CONTACT_CITY',
        'CONTACT_ST',
        'CONTACT_ZIP',
        'CONTACT_WEBSITE ',
        'NON_PROFIT',
        'EVENT_STARTDATE',
        'EVENT_ENDDATE',
        'EVENT_STARTTIME',
        'EVENT_ENDTIME',
        'EVENTDAY_CONTACT',
        'EVENTDAY_PHONE',
        'SETUP_STARTTIME',
        'BREAKDOWN_ENDTIME',
        'EVENT_TYPE',
        'PARTICIPANT_TYPE',
        'ANNUAL_EVENT',
        'EST_ATTENDANCE',
        'ALCOHOL',
        'FOOD',
        'TENTS_INFLATABLES',
        'BUS_IMPACT',
        'AMPLIFIED_MUSIC',
        'OPEN_FLAMES',
        'SPECIAL_EVENT_ZONE',
        'STATUS',
        'COMMENTS',
    ]

    PRODUCTION_ORG = forms.CharField(label="Organization")
    CONTACT_PHONE = forms.CharField(label="Phone")
    CONTACT_EMAIL = forms.CharField(label="Email")
    CONTACT_ADDRESS = forms.CharField(label="Address")
    CONTACT_CITY = forms.CharField(label="City")
    CONTACT_ST = forms.CharField(label="State")
    CONTACT_ZIP = forms.CharField(label="ZIP")
    CONTACT_WEBSITE = forms.CharField(label="Website")
    purpose = forms.CharField()
    NON_PROFIT = forms.BooleanField(label="Is the organization a non-profit?", required=False)
    beneficiary = forms.ChoiceField(choices=BENEFICIARY_CHOICES)
    CONTACT_NAME = forms.CharField(label="Contact Name")

    EVENT_NAME = forms.CharField(label="Event Name")
    LOCATION = forms.CharField(label="Location")
    date = forms.DateTimeField()
    ANNUAL_EVENT = CustomBooleanField(label="This is an annual event.", required=False)
    alternative_dates = forms.DateTimeField(required=False)
    EVENTDAY_CONTACT = forms.CharField(label="Event Day Contact")
    EVENT_STARTDATE = forms.CharField(label="Event Start Date")
    EVENT_ENDDATE = forms.CharField(label="Event End Date")
    EVENT_STARTTIME = forms.CharField(label="Event Start Time")
    EVENT_ENDTIME = forms.CharField(label="Event End Time")
    SETUP_STARTTIME = forms.CharField(label="Setup Start Time")
    BREAKDOWN_ENDTIME = forms.CharField(label="Breakdown End Time")
    route_description = forms.CharField()
    route_map = forms.FileField()
    route_url = forms.URLField()
    COMMENTS = forms.CharField()

    EVENT_TYPE = forms.MultipleChoiceField(choices=EVENT_TYPE_CHOICES)
    PARTICIPANT_TYPE = forms.CharField()
    EST_ATTENDANCE = forms.IntegerField(label="Estimated Attendance")
    previous_attendance = forms.IntegerField(required=False)
    previous_events = forms.ChoiceField(choices=PREVIOUS_EVENTS_CHOICES)

    trash_removal_plan = forms.CharField()
    updated_trash_removal_plan = forms.FileField()
    emergency_action_plan = forms.CharField()

    SPECIAL_EVENT_ZONE = forms.MultipleChoiceField(SPECIAL_ZONE_CHOICES)
    ALCOHOL = CustomBooleanField(label="There will be alcoholic beverages at this event.", required=False)
    FOOD = CustomBooleanField(label="The event will sell food.", required=False)
    TENTS_INFLATABLES = CustomBooleanField(label="There will be tents or inflatable structures in excess of 400 square feet.", required=False)
    BUS_IMPACT = forms.ChoiceField(label="This event impacts CAT or TTA bus routes.", required=False, choices=(('Yes', 'Yes'), ('No', 'No'), ('Unsure', 'Unsure')))
    AMPLIFIED_MUSIC = CustomBooleanField(label="There will be amplified music.", required=False)
    OPEN_FLAMES = CustomBooleanField(label="The event will involve fireworks, pyrotechnics or other open flame.", required=False)

    hold_harmless_agree = CustomBooleanField(label=HOLD_HARMLESS_TEXT)
    se_notif_reqs_agree = CustomBooleanField(label=SE_NOTIF_REQS_AGREE_TEXT)
    legal_agree = CustomBooleanField(label=LEGAL_AGREE_TEXT)
    app_fee_agree = CustomBooleanField(label=APP_FEE_AGREE_TEXT)

    def to_arcgis(self):

        data = {}

