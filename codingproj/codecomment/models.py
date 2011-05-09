# coding: utf-8
from django.db import models
from snippet.models import Snippet

class Comment(models.Model):
    snippet = models.ForeignKey(Snippet)
    lineno = models.IntegerField(u'行号')
    text = models.TextField(u'内容')

    @models.permalink
    def get_absolute_url(self):
        return ('comment_detail', (), {'pk': self.id})
