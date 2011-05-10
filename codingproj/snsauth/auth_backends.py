from django.contrib.auth.models import User
from django.conf import settings
from models import ExternalAccounts

class SnsBackend(object):
    supports_anonymous_user = False
    supports_object_permissions = False
    supports_inactive_user = False
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class DoubanBackend(SnsBackend):
    provider = 'douban'
    def authenticate(self, douban_token, user=None):
        from douban.service import DoubanService
        token = douban_token
        service = DoubanService(settings.SNS['douban']['app_key'],
                                settings.SNS['douban']['app_secret'])
        service.ProgrammaticLogin(token.key, token.secret)
        people = service.GetAuthorizedUID('/people/@me')
        username = people.uid.text+'@douban'
        user, created = User.objects.get_or_create(username=username)
        return user

class SinaBackend(SnsBackend):
    provider = 'sina'
    def authenticate(self, sina_token, user=None):
        from weibopy.auth import OAuthHandler
        from weibopy.api import API
        token = sina_token
        auth = OAuthHandler(settings.SNS['sina']['app_key'],
                            settings.SNS['sina']['app_secret'])
        auth.set_access_token(token.key, token.secret)
        username = auth.get_username()+'@sina'
        user, created = User.objects.get_or_create(username=username)
        return user

class QQBackend(SnsBackend):
    provider = 'qq'
    def authenticate(self, qq_token, user=None):
        username = qq_token.args['openid'][-10:]+'@qq'
        user, created = User.objects.get_or_create(username=username)
        return user
