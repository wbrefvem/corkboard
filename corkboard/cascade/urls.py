from django.conf.urls import patterns, url, include
from cascade import views

urlpatterns = patterns('',
    url(r'^$', views.LandingView.as_view(), {}, 'events-list'),

    url(r'^events/add/$', views.CreateEventView.as_view(), {}, 'event-add'),
    url(r'^events/update/$', views.UpdateEventView.as_view(), {}, 'event-update'),
    url(r'^events/delete/$', views.DeleteEventView.as_view(), {}, 'event-delete'),
    
    url(r'^organizations/add/$', views.CreateOrganizationView.as_view(), {}, 'organization-add'),

    url(r'^api/', include('cascade.api.urls')),
)
