from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings

from cascade import models, forms, tasks

import json


class FormViewMixin(FormView):

    def get_context_data(self, **kwargs):
        context = super(FormViewMixin, self).get_context_data(**kwargs)

        context.update({'url': reverse('event-add')})
        return context


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class BlobFormView(FormViewMixin):
    form_class = forms.BlobForm
    template_name = 'blob_form.html'
    success_url = '/blob/'

    def post(self, request, *args, **kwargs):

        form = forms.BlobForm(request.POST, request.FILES)

        if form.is_valid():
            form_data = dict((key, form.cleaned_data[key]) for key in form.ARC_GIS_FIELDS if key in form.cleaned_data)

            for key, value in form_data.items():
                if value:
                    form_data[key] = "Yes"
                else:
                    form_data[key] = "No"

                if type(value) is list:
                    form_data[key] = value[0]

            tasks.push_to_map.delay(form_data, form.cleaned_data['route_description'])

        return super(BlobFormView, self).post(request, *args, **kwargs)


class BlobView(TemplateView):
    template_name = 'blob.html'


class CreateEventView(LoginRequiredMixin, FormViewMixin):
    form_class = forms.SpecialEventForm
    template_name = 'create_event.html'
    success_url = '/cascade/events'

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


class CreateOrganizationView(LoginRequiredMixin, FormViewMixin):
    form_class = forms.OrganizationForm
    template_name = 'create_event.html'
    success_url = '/cascade/organizations/'


class LandingView(LoginRequiredMixin, TemplateView):
    template_name = 'landing.html'
