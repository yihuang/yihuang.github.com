from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^snippet/', include('snippet.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.MODE == 'dev':
    urlpatterns += staticfiles_urlpatterns()
