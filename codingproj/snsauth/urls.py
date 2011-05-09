from django.conf.urls.defaults import *

urlpatterns = patterns('snsauth.views',
    url(r'^douban_login/', 'douban_login', name='douban_login'),
    url(r'^douban_login_done/', 'douban_login_done', name='douban_login_done'),
)
