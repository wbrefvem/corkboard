from rest_framework import viewsets
from events import models
from events.api import serializers
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = serializers.ContentTypeSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class BeneficiaryViewSet(viewsets.ModelViewSet):
    queryset = models.Beneficiary.objects.all()
    serializer_class = serializers.BeneficiarySerializer


class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = models.EventType.objects.all()
    serializer_class = serializers.EventTypeSerializer


class ParticipationTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ParticipantType.objects.all()
    serializer_class = serializers.ParticipationTypeSerializer


class AltDateViewSet(viewsets.ModelViewSet):
    queryset = models.AltDate.objects.all()
    serializer_class = serializers.AltDateSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer


class SpecialEventViewSet(viewsets.ModelViewSet):
    queryset = models.SpecialEvent.objects.all()
    serializer_class = serializers.SpecialEventSerializer
