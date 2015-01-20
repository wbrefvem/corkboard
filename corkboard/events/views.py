from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from events import models
from events import forms

from django.conf import settings
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage


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


class CreateEventView(LoginRequiredMixin, FormView):
    form_class = forms.SpecialEventForm
    template_name = 'special_event_form.html'
    success_url = '/events/'



class UpdateEventView(LoginRequiredMixin, UpdateView):
    model = models.SpecialEvent
    template_name = 'update.html'
    fields = ['text']


class DeleteEventView(LoginRequiredMixin, DeleteView):
    pass


class EventListView(LoginRequiredMixin, ListView):
    model = models.SpecialEvent
    template_name = 'event_list.html'


class GoogleAuthRedirectView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        storage = Storage(models.CredentialsModel, 'id', self.request.user, 'credential')
        credential = storage.get()

        if credential is None or credential.invalid is True:
            OAUTH2_FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                           self.request.user)
            return OAUTH2_FLOW.step1_get_authorize_url()
        return super(GoogleAuthRedirectView, self).get_redirect_url(*args, **kwargs)


class GoogleAuthReturnRedirectView(LoginRequiredMixin, RedirectView):
    url = '/events'

    def get_redirect_url(self, *args, **kwargs):

        if not xsrfutil.validate_token(settings.SECRET_KEY, self.request.REQUEST['state'],
                                     self.request.user):
            return HttpResponseBadRequest()
        credential = OAUTH2_FLOW.step2_exchange(self.request.REQUEST)
        storage = Storage(models.CredentialsModel, 'id', self.request.user, 'credential')
        storage.put(credential)
        return super(GoogleAuthReturnRedirectView, self).get_redirect_url(*args, **kwargs)
