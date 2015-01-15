from django.conf.urls import patterns, url
from events import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^add/$', login_required(views.CreateEventView.as_view()), {}, 'event-add'),
    url(r'^update/$', login_required(views.UpdateEventView.as_view()), {}, 'event-update'),
    url(r'^delete/$', login_required(views.DeleteEventView.as_view()), {}, 'event-delete'),
)
