from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('snsauth.views',
    url(r'^douban/$', DoubanLoginView.as_view(), name='douban_login'),
    url(r'^sina/$', SinaLoginView.as_view(), name='sina_login'),
    url(r'^qq/$', QQLoginView.as_view(), name='qq_login'),
)
