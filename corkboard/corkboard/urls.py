from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('events.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^googleauth', views.GoogleAuthRedirectView.as_view(), {}, 'google-auth'),
    # url(r'^oauth2callback', views.GoogleAuthReturnRedirectView.as_view(), {}, 'oauth2-callback')
)
