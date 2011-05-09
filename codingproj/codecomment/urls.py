from django.conf.urls.defaults import *
from django.views.generic import ListView, CreateView, DetailView
from views import CommentCreateView
from models import Comment
from forms import CommentForm

urlpatterns = patterns('',
    url(r'^$',                      ListView.as_view(model=Comment),                name='comment_list'),
    url(r'^create$',                CommentCreateView.as_view(form_class=CommentForm, model=Comment),              name='comment_create'),
    url(r'^(?P<pk>\d+)$',                      DetailView.as_view(model=Comment),                name='comment_detail'),
)
