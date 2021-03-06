#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# code copied from https://github.com/siongui/webpy-oauth
#

from apps import auth
import os
import json
import dash


if "Users" in os.getcwd():
  secrets = 'secrets.json'
  with open(secrets) as f:
    secret = json.load(f)
  website = "http://localhost:8080"
  # create Google app & get app ID/secret from:
  # https://cloud.google.com/console
  auth.parameters['google']['app_id'] = secret["app_id"]
  auth.parameters['google']['app_secret'] = secret["app_secret"]
else:
  website = os.environ['website_URL']
  auth.parameters['google']['app_id'] = os.environ['app_id']
  auth.parameters['google']['app_secret'] = os.environ['app_secret']

# create Facebook app & get app ID/secret from:
# https://developers.facebook.com/apps
auth.parameters['facebook']['app_id'] = 'facebook-client-id'
auth.parameters['facebook']['app_secret'] = 'facebook-client-secret'


urls = (
  r"/", "LoginPage",
  r"/logout", "LogoutPage",
  r"/auth/(google|facebook)", "AuthPage",
  r"/auth/(google|facebook)/callback", "AuthCallbackPage",
)


class handler(auth.handler):
  def callback_uri(self, provider):
    """Please return appropriate url according to your app setting.
    """
    return '{}/auth/{}/callback'.format(website, provider)

  def on_signin(self, provider, profile):
    """Callback when the user successfully signs in the account of the provider
    (e.g., Google account or Facebook account).

    Arguments:
      provider: google or facebook
      profile: the user profile of Google or facebook account of the user who
               signs in.
    """
    # set cookies
    user_id = '%s:%s' % (provider, profile['id'])
    dash.callback_context.response.set_cookie('_id', user_id)
    dash.callback_context.response.set_cookie('_profile', json.dumps(profile))


class AuthPage(handler):
  def GET(self, provider):
    auth_url = self.auth_init(provider)
    return auth_url


class AuthCallbackPage(handler):
  def GET(self, provider, code):
    self.auth_callback(provider, code)


class LoginPage:
  def GET(self):
    return


class LogoutPage:
  def GET(self):
    dash.callback_context.response.set_cookie('_id', '')
    dash.callback_context.response.set_cookie('_profile', '')
    # invalidate '_id' in the cookie to logout the user

