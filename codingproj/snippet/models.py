# coding: utf-8
from django.contrib.auth.models import User
from django.db import models
import tagging
from formatter import formatter

PROGRAMMING_LANGUAGES = (
    (1, 'python'),
    (2, 'haskell'),
)

class Snippet(models.Model):
    user = models.ForeignKey(User)
    language = models.IntegerField(u'编程语言', choices=PROGRAMMING_LANGUAGES)
    orign = models.TextField(u'代码')
    formatted = models.TextField(u'格式化代码', null=True, editable=False)
    public = models.BooleanField(u'是否公开', default=True, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('snippet_view', (), {'pk': self.pk})

    def get_style(self):
        return formatter.get_style_defs()

tagging.register(Snippet)
