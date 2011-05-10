# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField

SNS_PROVIDER = (
    ('douban', u'豆瓣'),
    ('sina', u'新浪围脖'),
    ('qq', u'腾讯'),
)

class ExternalAccounts(models.Model):
    '''
    关联外部帐号
    '''
    user = models.OneToOneField(User)
    key = models.CharField(u'唯一标识', max_length=256)
    provider = models.CharField(u'SNS服务', max_length=32, choices=SNS_PROVIDER)
    nickname = models.CharField(u'昵称', max_length=255, default='')
    avatar = models.URLField(u'头像地址', default='')
    access_token = PickledObjectField(u'token', null=True, blank=True)

    class Meta:
        unique_together = ('key', 'provider')
