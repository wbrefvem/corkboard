from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings

from cascade import models, forms, tasks

from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage
from googleapiclient.discovery import build

import httplib2
import json


OAUTH2_FLOW = flow_from_clientsecrets(
    settings.GOOGLE_CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri=settings.GOOGLE_REDIRECT_URI
)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class BlobFormView(FormView):
    form_class = forms.BlobForm
    template_name = 'blob_form.html'
    success_url = '/blob/'

    def get_context_data(self, **kwargs):
        context = super(BlobFormView, self).get_context_data(**kwargs)

        context.update({'url': reverse('blob-form')})
        return context

    def post(self, request, *args, **kwargs):

        form = forms.BlobForm(request.POST, request.FILES)

        if form.is_valid():
            form_data = dict((key, form.cleaned_data[key]) for key in form.ARC_GIS_FIELDS if key in form.cleaned_data)

            for key,value in form_data.items():
                if value == True:
                    form_data [key] = "Yes"
                elif value == False:
                    form_data[key] = "No"

                if type(value) is list:
                    form_data[key] = value[0]

            arcgis_data = [
                {
                    "geometry": {
                          "paths" : [[[-97.06138,32.837],[-97.06133,32.836],[-97.06124,32.834],[-97.06127,32.832]], 
                                     [[-97.06326,32.759],[-97.06298,32.755]]],
                          "spatialReference" : {"wkid" : 4326}
                    },
                    "attributes": form_data
                }
            ]

            print(json.dumps(arcgis_data))

            tasks.push_to_map.delay('http://mapstest.raleighnc.gov/arcgis/rest/services/SpecialEvents/FeatureServer/0/addFeatures', arcgis_data)
        return super(BlobFormView, self).post(request, *args, **kwargs)


class BlobView(TemplateView):
    template_name = 'blob.html'


class CreateEventView(LoginRequiredMixin, FormView):
    form_class = forms.SpecialEventForm
    template_name = 'create_event.html'
    success_url = '/cascade/events'

    def get_context_data(self, **kwargs):
        context = super(CreateEventView, self).get_context_data(**kwargs)

        context.update({'url': reverse('event-add')})
        return context

    def post(self, request, *args, **kwargs):

        return super(CreateEventView, self).post(request, *args, **kwargs)


class UpdateEventView(LoginRequiredMixin, UpdateView):
    model = models.SpecialEvent
    template_name = 'update.html'
    fields = ['text']


class DeleteEventView(LoginRequiredMixin, DeleteView):
    pass


class EventListView(LoginRequiredMixin, ListView):
    model = models.SpecialEvent
    template_name = 'event_list.html'


class CreateOrganizationView(LoginRequiredMixin, FormView):
    form_class = forms.OrganizationForm
    template_name = 'create_event.html'
    success_url = '/cascade/organizations/'

    def get_context_data(self, **kwargs):
        context = super(CreateOrganizationView, self).get_context_data(**kwargs)

        context.update({'url': reverse('organization-add')})
        return context


class LandingView(LoginRequiredMixin, TemplateView):
    template_name = 'landing.html'


class GoogleAuthRedirectView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        storage = Storage(models.CredentialsModel, 'id', self.request.user, 'credential')
        credential = storage.get()

        if credential is None or (type(credential) is not bytes and getattr(credential, 'invalid', True) is True):
            OAUTH2_FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                           self.request.user)
            return OAUTH2_FLOW.step1_get_authorize_url()
        else:
            http = httplib2.Http()
            http = credential.authorize(http)
            service = build("calendar", "v3", http=http)
            activities = service.activities()
            activitylist = activities.list(collection='public',
                                           userId='me').execute()
            print(activitylist)
            return super(GoogleAuthRedirectView, self).get_redirect_url(*args, **kwargs)


class GoogleAuthReturnRedirectView(LoginRequiredMixin, RedirectView):
    url = '/events'

    def get_redirect_url(self, *args, **kwargs):

        if not xsrfutil.validate_token(settings.SECRET_KEY, self.request.REQUEST['state'], self.request.user):
            return HttpResponseBadRequest()
        credential = OAUTH2_FLOW.step2_exchange(self.request.REQUEST)
        storage = Storage(models.CredentialsModel, 'id', self.request.user, 'credential')
        storage.put(credential)
        return super(GoogleAuthReturnRedirectView, self).get_redirect_url(*args, **kwargs)
