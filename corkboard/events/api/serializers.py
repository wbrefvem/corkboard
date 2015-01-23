from events import models
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission


class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentType


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Address


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Contact


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Organization


class BeneficiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Beneficiary


class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EventType


class ParticipationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ParticipantType


class AltDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AltDate


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Area


class SpecialEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SpecialEvent
