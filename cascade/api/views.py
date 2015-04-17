from rest_framework import viewsets
from cascade import models
from cascade.api import serializers, renderers
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class BaseViewSet(viewsets.ModelViewSet):
    renderer_classes = (renderers.JSONRenderer,)


class UserViewSet(BaseViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class GroupViewSet(BaseViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class PermissionViewSet(BaseViewSet):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


class ContentTypeViewSet(BaseViewSet):
    queryset = ContentType.objects.all()
    serializer_class = serializers.ContentTypeSerializer


class AddressViewSet(BaseViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class ContactViewSet(BaseViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class OrganizationViewSet(BaseViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class BeneficiaryViewSet(BaseViewSet):
    queryset = models.Beneficiary.objects.all()
    serializer_class = serializers.BeneficiarySerializer


class EventTypeViewSet(BaseViewSet):
    queryset = models.EventType.objects.all()
    serializer_class = serializers.EventTypeSerializer


class ParticipationTypeViewSet(BaseViewSet):
    queryset = models.ParticipantType.objects.all()
    serializer_class = serializers.ParticipationTypeSerializer


class AltDateViewSet(BaseViewSet):
    queryset = models.AltDate.objects.all()
    serializer_class = serializers.AltDateSerializer


class AreaViewSet(BaseViewSet):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer


class SpecialEventViewSet(BaseViewSet):
    queryset = models.SpecialEvent.objects.all()
    serializer_class = serializers.SpecialEventSerializer

class RouteViewSet(BaseViewSet):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
