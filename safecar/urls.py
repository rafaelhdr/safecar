from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'web.views.home', name='home'),
    url(r'^dashboard$', 'web.views.dashboard', name='dashboard'),
    url(r'^map$', 'web.views.map', name='map'),

    url(r'^admin/', include(admin.site.urls)),
)
