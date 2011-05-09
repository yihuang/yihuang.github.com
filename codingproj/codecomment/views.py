from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import CreateView,
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.list import MultipleObjectTemplateResponseMixin

class JsonResponse(object):
    def __init__(self, request, template_names, context, **kwargs):
        pass

class RestResponseMixin(TemplateResponseMixin):

    def render_to_response(self, context):
        self.response_class = self.get_response_class()
        return super(RestResponseMixin, self).render_to_response(context)

    def get_response_class(self):
        fmt = self.kwargs.get('format', 'html')
        return {
            'html': TemplateResponse,
            'json': JsonResponse,
            'jsonp': JsonpResponse,
        }[fmt]

class MultipleObjectRestResponseMixin(MultipleObjectTemplateResponseMixin, RestResponseMixin):
    pass

class CommentCreateView(CreateView):
    def get_initial(self):
        return {
            'snippet': self.request.GET.get('snippet'),
            'lineno': self.request.GET.get('lineno'),
        }
