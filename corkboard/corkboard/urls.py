from django.conf.urls import patterns, include, url
from django.contrib import admin
from events import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('events.urls')),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', {}, 'login'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', {}, 'logout'),
    url(r'^googleauth', views.GoogleAuthRedirectView.as_view(), {}, 'google-auth'),
    url(r'^oauth2callback', views.GoogleAuthReturnRedirectView.as_view(), {}, 'oauth2-callback')
)
