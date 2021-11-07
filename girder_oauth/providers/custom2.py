# -*- coding: utf-8 -*-
import urllib.parse

import jwt

from girder.api.rest import getApiUrl
from girder.exceptions import RestException
from girder.models.setting import Setting

from .base import ProviderBase
from ..settings import PluginSettings

class Custom2(ProviderBase):
    def getClientIdSetting(self):
        return Setting().get(PluginSettings.CUSTOM2_CLIENT_ID)

    def getClientSecretSetting(self):
        return Setting().get(PluginSettings.CUSTOM2_CLIENT_SECRET)

    @classmethod
    def getClientAuthUrl(cls):
        return Setting().get(PluginSettings.CUSTOM2_CLIENT_AUTH_URL)

    def getClientTokenUrl(self):
        return Setting().get(PluginSettings.CUSTOM2_CLIENT_TOKEN_URL)

    @classmethod
    def getClientScope(cls):
        return Setting().get(PluginSettings.CUSTOM2_CLIENT_SCOPE)
    
    @classmethod
    def getClientButtonColor(cls):
        color = Setting().get(PluginSettings.CUSTOM2_CLIENT_BUTTON_COLOR)
        return color.split(';')

    @classmethod
    def getClientIconUrl(cls):
        return Setting().get(PluginSettings.CUSTOM2_CLIENT_ICON_URL)

    @classmethod
    def getClientName(cls):
        return Setting().get(PluginSettings.CUSTOM2_CLIENT_NAME)

    @classmethod
    def getUrl(cls, state):
        clientId = Setting().get(PluginSettings.CUSTOM_CLIENT_ID)
        if not clientId:
            raise Exception('No Custom client ID setting is present.')

        callbackUrl = '/'.join((getApiUrl(), 'oauth', 'custom2', 'callback'))

        query = urllib.parse.urlencode({
            'response_type': 'code',
            'client_id': clientId,
            'redirect_uri': callbackUrl,
            'state': state,
            'scope': '%s' % cls.getClientScope()
        })
        return '%s?%s' % (cls.getClientAuthUrl(), query)

    def getToken(self, code):
        params = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'redirect_uri': self.redirectUri
        }
        resp = self._getJson(method='POST', url=self.getClientTokenUrl(),
                             data=params,
                             headers={'Accept': 'application/json'})
        if 'error' in resp:
            raise RestException(
                'Got an error exchanging token from provider: "%s".' % resp,
                code=502)
        return resp

    def getUser(self, token):
        idToken = token['id_token']

        payload = jwt.decode(idToken, verify=False)

        oauthId = payload['sub']

        email = payload.get('email')
        if not email:
            raise RestException('This user has no available email address.', code=502)

        firstName = payload.get('given_name')
        lastName = payload.get('family_name')

        user = self._createOrReuseUser(oauthId, email, firstName, lastName)
        return user
