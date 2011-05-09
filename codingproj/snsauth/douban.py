import os, sys, httplib
from oauth import oauth

APP_KEY = '021e921e86db109c065bb65b949131d4'
APP_SECRET = '6be5d7dce18883b8'
request_token_url = 'http://www.douban.com/service/auth/request_token'
auth_url = 'http://www.douban.com/service/auth/authorize'
access_token_url = 'http://www.douban.com/service/auth/access_token'

consumer = oauth.OAuthConsumer(APP_KEY, APP_SECRET)
conn = httplib.HTTPConnection('douban.com:80')

def login():
    req = oauth.OAuthRequest.from_consumer_and_token(consumer,
            callback='/',
            http_url=request_token_url)
    req.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, None)

    conn.request(req.http_method, req.http_url, headers=req.to_header())
    token = oauth.OAuthToken.from_string( conn.getresponse().read() )

    req = oauth.OAuthRequest.from_token_and_callback(token=token, http_url=auth_url, callback='http://www.jjmmw.com/')
    print req.to_url()
    os.system('google-chrome "%s"'%req.to_url())

def login_done(token):
    req = oauth.OAuthRequest.from_consumer_and_token(consumer, token=token, http_url=access_token_url)
    req.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    conn.request(req.http_method, req.http_url, headers=req.to_header())
    token = oauth.OAuthToken.from_string( conn.getresponse().read() )
