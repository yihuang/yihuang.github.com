from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^snippet/', include('snippet.urls')),
    (r'^comment/', include('codecomment.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('snsauth.urls')),
    #(r'^accounts/', include('socialauth.urls')),
    (r'^$', 'socialauth.views.signin_complete'),
)

if settings.MODE == 'dev':
    urlpatterns += staticfiles_urlpatterns()
