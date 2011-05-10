# coding: utf-8
import logging
logger = logging.getLogger('root')

import os, sys, httplib, urlparse, pickle
from urllib import splithost, splittype
from oauth import oauth
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import View

from models import ExternalAccounts

def splithost2(url):
    return splithost(splittype(url)[1])

def dorequest(conn, req, send_header=False):
    if send_header:
        headers = req.to_headers()
    else:
        headers = {}

    host, path = splithost2(req.to_url())
    headers['Host'] = host

    conn.request(req.http_method, path, headers=headers)
    rep = conn.getresponse()
    content = rep.read()
    logger.info('request %s%s -> %s' % (host, path, content))
    if rep.status == 200:
        return content
    else:
        logger.error('request fail, %s%s -> %d %s'%(host, path, rep.status, content))
        return content

class NewUserForm(forms.Form):
    username = forms.CharField(label=u'用户名', max_length=30)
    email = forms.EmailField(label=u'邮箱')
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(u'该用户名已被注册，请换一个。')

class OAuthLoginView(View):
    host            = None
    port            = 80

    app_key         = None
    app_secret      = None

    request_token_url = None
    authorize_url   = None
    access_token_url = None

    callback_arg    = 'oauth_token'
    verifier_arg    = None
    redirect_arg    = 'next'
    authbackend_arg = None

    def get(self, request, *args, **kwargs):
        consumer = oauth.OAuthConsumer(self.app_key, self.app_secret)
        conn = httplib.HTTPConnection(self.host, self.port)

        request_key = request.GET.get(self.callback_arg)
        if not request_key:
            next = request.GET.get(self.redirect_arg)
            if next:
                request.session['oauth_login_redirect'] = next
            # fetch request token
            req = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    http_url=self.request_token_url)
            req.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, None)
            rep = dorequest(conn, req)
            token = oauth.OAuthToken.from_string(rep)
            request.session['oauth_request_token'] = token

            # fetch authorize url
            req = oauth.OAuthRequest.from_token_and_callback(token=token, http_url=self.authorize_url, callback=request.build_absolute_uri(), parameters={'oauth_consumer_key': self.app_key})
            return HttpResponseRedirect(req.to_url())
        else:
            # authorize callbacked, fetch access token
            token = request.session['oauth_request_token']
            del request.session['oauth_request_token']
            assert token.key == request_key, token
            if self.verifier_arg:
                verifier = request.GET.get(self.verifier_arg)
            else:
                verifier = None
            req = oauth.OAuthRequest.from_consumer_and_token(consumer, token=token, http_url=self.access_token_url, parameters={self.verifier_arg: verifier})
            req.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
            rep = dorequest(conn, req)
            token = oauth.OAuthToken.from_string(rep)
            token.args = request.REQUEST
            try:
                acc = ExternalAccounts.objects.get(provider=self.provider, key=self.get_uid(token))
            except ExternalAccounts.DoesNotExist:
                request.session['oauth_access_token'] = token
                return render(request, 'snsauth/connect_accounts.html', {
                    'newuserform': NewUserForm(),
                    'existuserform': AuthenticationForm(),
                })
            else:
                acc.access_token = token
                acc.save()
                self.login(request, acc.user)
                return self.success(request)

    def login(self, request, u):
        u.backend = 'django.contrib.auth.backends.ModelBackend'
        return login(request, u)

    def success(self, request):
        if request.session.has_key('oauth_login_redirect'):
            next = request.session['oauth_login_redirect']
            del request.session['oauth_login_redirect']
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        '''
        创建账户或关联现有账户
        '''
        token = request.session['oauth_access_token']

        if 'newuser' in request.POST:
            form = NewUserForm(data=request.POST)
        else:
            form = AuthenticationForm(data=request.POST)

        if not form.is_valid():
            if isinstance(form, NewUserForm):
                return render(request, 'snsauth/connect_accounts.html', {
                    'newuserform':      form,
                    'existuserform':    AuthenticationForm(),
                })
            else:
                return render(request, 'snsauth/connect_accounts.html', {
                    'newuserform':      NewUserForm(),
                    'existuserform':    form,
                })
        else:
            if isinstance(form, AuthenticationForm):
                user = form.get_user()
            else:
                user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'])
                # register info TODO

            # connect user
            uid, nickname, avatar = self.get_info(token)
            ExternalAccounts(user=user, key=uid, provider=self.provider, nickname=nickname, avatar=avatar, access_token=token).save()
            self.login(request, user)
            return self.success(request)

class DoubanLoginView(OAuthLoginView):
    provider            = 'douban'
    app_key             = settings.SNS['douban']['app_key']
    app_secret          = settings.SNS['douban']['app_secret']
    host                = 'douban.com'
    request_token_url   = 'http://www.douban.com/service/auth/request_token'
    authorize_url       = 'http://www.douban.com/service/auth/authorize'
    access_token_url    = 'http://www.douban.com/service/auth/access_token'
    authbackend_arg     = 'douban_token'

    def get_me(self, token):
        from douban.service import DoubanService
        service = DoubanService(settings.SNS['douban']['app_key'],
                                settings.SNS['douban']['app_secret'])
        service.ProgrammaticLogin(token.key, token.secret)
        return service.GetAuthorizedUID('/people/@me')

    def get_uid(self, token):
        people = self.get_me(token)
        return people.uid.text

    def get_info(self, token):
        people = self.get_me(token)
        return people.uid.text, people.uid.text, ''

class SinaLoginView(OAuthLoginView):
    provider            = 'sina'
    app_key             = settings.SNS['sina']['app_key']
    app_secret          = settings.SNS['sina']['app_secret']
    host                = 'api.t.sina.com.cn'
    request_token_url   = 'http://api.t.sina.com.cn/oauth/request_token'
    authorize_url       = 'http://api.t.sina.com.cn/oauth/authorize'
    access_token_url    = 'http://api.t.sina.com.cn/oauth/access_token'
    verifier_arg        = 'oauth_verifier'
    authbackend_arg     = 'sina_token'

    def get_uid(self, token):
        from weibopy.auth import OAuthHandler
        from weibopy.api import API
        auth = OAuthHandler(settings.SNS['sina']['app_key'],
                            settings.SNS['sina']['app_secret'])
        auth.set_access_token(token.key, token.secret)
        return auth.get_username()

    def get_info(self, token):
        key = self.get_uid(token)
        return key, key, ''

class QQLoginView(OAuthLoginView):
    provider            = 'qq'
    app_key             = settings.SNS['qq']['app_key']
    app_secret          = settings.SNS['qq']['app_secret']
    host                = 'openapi.qzone.qq.com'
    request_token_url   = 'http://openapi.qzone.qq.com/oauth/qzoneoauth_request_token'
    authorize_url       = 'http://openapi.qzone.qq.com/oauth/qzoneoauth_authorize'
    access_token_url    = 'http://openapi.qzone.qq.com/oauth/qzoneoauth_access_token'
    verifier_arg        = 'oauth_vericode'
    authbackend_arg     = 'qq_token'

    def get_uid(self, token):
        return token['openid']
    def get_info(self, token):
        # TODO
        key = self.get_uid(token)
        return key, key, ''

