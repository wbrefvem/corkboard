from django.conf.urls import url, include
from rest_framework import routers
from cascade.api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'permissions', views.PermissionViewSet)
router.register(r'content-types', views.ContentTypeViewSet)
router.register(r'addresses', views.AddressViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'beneficiaries', views.BeneficiaryViewSet)
router.register(r'event-types', views.EventTypeViewSet)
router.register(r'participation-types', views.ParticipationTypeViewSet)
router.register(r'alt-dates', views.AltDateViewSet)
router.register(r'areas', views.AreaViewSet)
router.register(r'special-events', views.SpecialEventViewSet)
router.register(r'routes', views.RouteViewSet)

urlpatterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
