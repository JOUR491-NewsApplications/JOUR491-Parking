from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tickets.views.home', name='home'),
    url(r'^locations/(?P<slug>[-\w]+)/$', 'tickets.views.locationdetail', name='locationdetail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
