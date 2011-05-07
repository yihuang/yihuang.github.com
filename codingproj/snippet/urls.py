from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from forms import SnippetForm
from models import Snippet
import views

urlpatterns = patterns('',
    url(r'^$',                      ListView.as_view(model=Snippet),                name='snippet_list'),
    url(r'^create$',                CreateView.as_view(form_class=SnippetForm, model=Snippet),      name='snippet_create'),
    url(r'^(?P<pk>\d+)$',           DetailView.as_view(model=Snippet),              name='snippet_view'),
    url(r'^(?P<pk>\d+)/edit$',      UpdateView.as_view(form_class=SnippetForm, model=Snippet),      name='snippet_edit'),
    url(r'^(?P<pk>\d+)/delete$',    DeleteView.as_view(model=Snippet),              name='snippet_delete'),
)
