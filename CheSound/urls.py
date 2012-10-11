from django.conf.urls import patterns, include, url
#from CheSound.views import index
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CheSound.views.home', name='home'),
    # url(r'^CheSound/', include('CheSound.foo.urls')),
    url(r'^$', 'frontend.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
