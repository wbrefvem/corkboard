from cascade import models
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address


class ContactSerializer(serializers.ModelSerializer):
    cell = serializers.CharField()
    telephone = serializers.CharField()

    class Meta:
        model = models.Contact


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beneficiary


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventType


class ParticipationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParticipantType


class AltDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AltDate


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Area


class SpecialEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpecialEvent


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
