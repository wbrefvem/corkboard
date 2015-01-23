from django.conf.urls import patterns, url, include
from events import views

urlpatterns = patterns('',
    url(r'^$', views.EventListView.as_view(), {}, 'events-list'),
    url(r'^add/$', views.CreateEventView.as_view(), {}, 'event-add'),
    url(r'^update/$', views.UpdateEventView.as_view(), {}, 'event-update'),
    url(r'^delete/$', views.DeleteEventView.as_view(), {}, 'event-delete'),
    url(r'^api/', include('events.api.urls'))
)
