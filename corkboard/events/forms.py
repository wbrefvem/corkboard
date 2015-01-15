from django import forms
from corkboard.events import models


class ApproveEventForm(forms.ModelForm):
    model = models.SpecialEvent
    fields
