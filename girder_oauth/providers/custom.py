# -*- coding: utf-8 -*-
import urllib.parse

import jwt

from girder.api.rest import getApiUrl
from girder.exceptions import RestException
from girder.models.setting import Setting

from .base import ProviderBase
from ..settings import PluginSettings
import logging

class Custom(ProviderBase):
    def getClientIdSetting(self):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_ID)

    def getClientSecretSetting(self):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_SECRET)

    @classmethod
    def getClientAuthUrl(cls):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_AUTH_URL)

    def getClientTokenUrl(self):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_TOKEN_URL)

    @classmethod
    def getClientScope(cls):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_SCOPE)
    
    @classmethod
    def getClientButtonColor(cls):
        color = Setting().get(PluginSettings.CUSTOM_CLIENT_BUTTON_COLOR)
        return color.split(';')

    @classmethod
    def getClientIconUrl(cls):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_ICON_URL)

    @classmethod
    def getClientName(cls):
        return Setting().get(PluginSettings.CUSTOM_CLIENT_NAME)

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

        logging.warning("custom.py: (getUser) Line 82 - token: %s", token)

        payload = jwt.decode(idToken, verify=False)

        logging.warning("custom.py: (getUser) Line 86 - payload: %s", payload)

        oauthId = payload['sub']

        logging.warning("custom.py: (getUser) Line 90 - oauthId: %s", oauthId)

        email = payload.get('email')
        
        if not email:
            raise RestException('This user has no available email address.', code=502)

        firstName = payload.get('given_name')
        lastName = payload.get('family_name')

        logging.warning("custom.py: (getUser) Line 100 - firstName: %s", firstName)
        logging.warning("custom.py: (getUser) Line 101 - lastName: %s", lastName)

        user = self._createOrReuseUser(oauthId, email, firstName, lastName)

        logging.warning("custom.py: (getUser) Line 105 - user: %s", user)
        
        return user
