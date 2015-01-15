from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import RedirectView
from events import models

from django.conf import settings
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage


class CreateEventView(CreateView):
    model = models.SpecialEvent
    template_name = 'create.html'
    fields = ['text']

    def post(self, request, *args, **kwargs):
        print('giggity')
        return super(CreateEventView, self).post(request, *args, **kwargs)


class UpdateEventView(UpdateView):
    model = models.SpecialEvent
    template_name = 'update.html'
    fields = ['text']


class DeleteEventView(DeleteView):
    pass


class GoogleAuthRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        flow = self.initialize_oauth2_flow()
        storage = Storage(models.CredentialsModel, 'id', self.request.user, 'credential')
        credential = storage.get()

        if credential is None or credential.invalid is True:
            flow.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                           self.request.user)
            return flow.step1_get_authorize_url()
        return super(GoogleAuthRedirectView, self).get_redirect_url(*args, **kwargs)

    def initialize_oauth2_flow(self):
        return flow_from_clientsecrets(
            settings.GOOGLE_CLIENT_SECRETS,
            scope='https://www.googleapis.com/auth/calendar',
            redirect_uri='http://localhost:8008/oauth2callback'
        )


class GoogleAuthReturnRedirectView(RedirectView):
    url = '/events/update'

    def get_redirect_url(self, *args, **kwargs):

        kwargs.update({'pk': self.request.GET.get('pk')})
        return super(GoogleAuthReturnRedirectView, self).get_redirect_url(*args, **kwargs)
