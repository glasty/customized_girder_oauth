# -*- coding: utf-8 -*-
import urllib.parse

import jwt

from girder.api.rest import getApiUrl
from girder.exceptions import RestException
from girder.models.setting import Setting

from .base import ProviderBase
from ..settings import PluginSettings

class Custom(ProviderBase):
    _AUTH_URL = 'https://api.login.yahoo.com/oauth2/request_auth'
    _AUTH_SCOPES = ['profile', 'email', 'sdps-r']
    _TOKEN_URL = 'https://api.login.yahoo.com/oauth2/get_token'

    def getClientIdSetting(self):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_ID)

    def getClientSecretSetting(self):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_SECRET)

    @classmethod
    def getUrl(cls, state):
        clientId = Setting().get(PluginSettings.CUSTOM_CLIENT_ID)
        if not clientId:
            raise Exception('No Custom client ID setting is present.')

        callbackUrl = '/'.join((getApiUrl(), 'oauth', 'custom', 'callback'))

        query = urllib.parse.urlencode({
            'response_type': 'code',
            'client_id': clientId,
            'redirect_uri': callbackUrl,
            'state': state,
            'scope': 'openid %s' % ' '.join(cls._AUTH_SCOPES)
        })
        return '%s?%s' % (cls._AUTH_URL, query)

    def getToken(self, code):
        params = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'redirect_uri': self.redirectUri
        }
        resp = self._getJson(method='POST', url=self._TOKEN_URL,
                             data=params,
                             headers={'Accept': 'application/json'})
        if 'error' in resp:
            raise RestException(
                'Got an error exchanging token from provider: "%s".' % resp,
                code=502)
        return resp

    def getUser(self, token):
        idToken = token['id_token']

        # Because the token came directly from Google's API, we don't need to verify it
        payload = jwt.decode(idToken, verify=False)

        oauthId = payload['sub']

        email = payload.get('email')
        if not email:
            raise RestException('This user has no available email address.', code=502)

        firstName = payload.get('given_name')
        lastName = payload.get('last_name')

        user = self._createOrReuseUser(oauthId, email, firstName, lastName)
        return user