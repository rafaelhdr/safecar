from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'web.views.home', name='home'),
    url(r'^dashboard$', 'web.views.dashboard', name='dashboard'),
    url(r'^map$', 'web.views.map', name='map'),
    url(r'^map-iframe$', 'web.views.map_iframe', name='map_iframe'),
    url(r'^api/car/mark-status$', 'web.views.mark_status', name='mark_status'),
    url(r'^api/car/set-location$', 'web.views.set_location', name='set_location'),
    url(r'^api/login$', 'web.views.api_login', name='api_login'),

    url(r'^admin/', include(admin.site.urls)),
)
