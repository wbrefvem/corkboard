from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from oauth2client.django_orm import CredentialsField


class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    credential = CredentialsField()


class SpecialEvent(models.Model):
    text = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
            return reverse('event-update', kwargs={'pk': self.pk})
