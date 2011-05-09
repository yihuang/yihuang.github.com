from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from douban.client import OAuthClient
from douban.service import DoubanService

API_KEY = '021e921e86db109c065bb65b949131d4'
SECRET = '6be5d7dce18883b8'

def authenticate(acctoken, accsecret):
    service = DoubanService(api_key=API_KEY, secret=SECRET)
    service.ProgrammaticLogin(acctoken, accsecret)
    user = service.GetAuthorizedUID('/people/@me')

def douban_login(request):
    client = OAuthClient(key=API_KEY, secret=SECRET)
    key, secret = client.get_request_token()
    url = client.get_authorization_url(key, secret, callback=reverse('douban_login_done'))
    return HttpResponseRedirect(url)

def douban_login_done(request):
    token = request.PARAMS.get('oauth_token')
    if not token:
        return HttpResponseRedirect('douban_login')
    client = OAuthClient(key=API_KEY, secret=SECRET)
    acctoken, accsecret = client.get_access_token(token, secret)
    request.session['douban_access_token'] = (acctoken, accsecret)
    user = authenticate(acctoken, accsecret)
    if user:
        login(request, user)
    return HttpResponseRedirect('/')
