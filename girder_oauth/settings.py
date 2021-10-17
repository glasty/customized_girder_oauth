from girder.exceptions import ValidationException
from girder.utility import setting_utilities


class PluginSettings:
    PROVIDERS_ENABLED = 'oauth.providers_enabled'
    IGNORE_REGISTRATION_POLICY = 'oauth.ignore_registration_policy'

    GOOGLE_CLIENT_ID = 'oauth.google_client_id'
    GOOGLE_CLIENT_SECRET = 'oauth.google_client_secret'
    GOOGLE_CLIENT_AUTH_URL = 'oauth.google_client_auth_url'
    GOOGLE_CLIENT_TOKEN_URL = 'oauth.google_client_token_url',
    GOOGLE_CLIENT_SCOPE = 'oauth.google_client_scope',

    GLOBUS_CLIENT_ID = 'oauth.globus_client_id'
    GLOBUS_CLIENT_SECRET = 'oauth.globus_client_secret'
    GLOBUS_CLIENT_AUTH_URL = 'oauth.globus_client_auth_url'
    GLOBUS_CLIENT_TOKEN_URL = 'oauth.globus_client_token_url',
    GLOBUS_CLIENT_SCOPE = 'oauth.globus_client_scope',

    GITHUB_CLIENT_ID = 'oauth.github_client_id'
    GITHUB_CLIENT_SECRET = 'oauth.github_client_secret'
    GITHUB_CLIENT_AUTH_URL = 'oauth.github_client_auth_url'
    GITHUB_CLIENT_TOKEN_URL = 'oauth.github_client_token_url',
    GITHUB_CLIENT_SCOPE = 'oauth.github_client_scope',

    LINKEDIN_CLIENT_ID = 'oauth.linkedin_client_id'
    LINKEDIN_CLIENT_SECRET = 'oauth.linkedin_client_secret'
    LINKEDIN_CLIENT_AUTH_URL = 'oauth.linkedin_client_auth_url'
    LINKEDIN_CLIENT_TOKEN_URL = 'oauth.linkedin_client_token_url',
    LINKEDIN_CLIENT_SCOPE = 'oauth.linkedin_client_scope',

    BITBUCKET_CLIENT_ID = 'oauth.bitbucket_client_id'
    BITBUCKET_CLIENT_SECRET = 'oauth.bitbucket_client_secret'
    BITBUCKET_CLIENT_AUTH_URL = 'oauth.bitbucket_client_auth_url'
    BITBUCKET_CLIENT_TOKEN_URL = 'oauth.bitbucket_client_token_url',
    BITBUCKET_CLIENT_SCOPE = 'oauth.bitbucket_client_scope',

    BOX_CLIENT_ID = 'oauth.box_client_id'
    BOX_CLIENT_SECRET = 'oauth.box_client_secret'
    BOX_CLIENT_AUTH_URL = 'oauth.box_client_auth_url'
    BOX_CLIENT_TOKEN_URL = 'oauth.box_client_token_url',
    BOX_CLIENT_SCOPE = 'oauth.box_client_scope',

    CUSTOM_CLIENT_ID = 'oauth.custom_client_id'
    CUSTOM_CLIENT_SECRET = 'oauth.custom_client_secret'
    CUSTOM_CLIENT_AUTH_URL = 'oauth.custom_client_auth_url'
    CUSTOM_CLIENT_TOKEN_URL = 'oauth.custom_client_token_url',
    CUSTOM_CLIENT_SCOPE = 'oauth.custom_client_scope',



@setting_utilities.default(PluginSettings.PROVIDERS_ENABLED)
def _defaultProvidersEnabled():
    return []


@setting_utilities.default(PluginSettings.IGNORE_REGISTRATION_POLICY)
def _defaultIgnoreRegistrationPolicy():
    return False


@setting_utilities.default({
    PluginSettings.GOOGLE_CLIENT_ID,
    PluginSettings.GLOBUS_CLIENT_ID,
    PluginSettings.GITHUB_CLIENT_ID,
    PluginSettings.LINKEDIN_CLIENT_ID,
    PluginSettings.BITBUCKET_CLIENT_ID,
    PluginSettings.BOX_CLIENT_ID,
    PluginSettings.CUSTOM_CLIENT_ID,
    PluginSettings.GOOGLE_CLIENT_SECRET,
    PluginSettings.GLOBUS_CLIENT_SECRET,
    PluginSettings.GITHUB_CLIENT_SECRET,
    PluginSettings.LINKEDIN_CLIENT_SECRET,
    PluginSettings.BITBUCKET_CLIENT_SECRET,
    PluginSettings.BOX_CLIENT_SECRET,
    PluginSettings.CUSTOM_CLIENT_SECRET,
    PluginSettings.GOOGLE_CLIENT_AUTH_URL,
    PluginSettings.GLOBUS_CLIENT_AUTH_URL,
    PluginSettings.GITHUB_CLIENT_AUTH_URL,
    PluginSettings.LINKEDIN_CLIENT_AUTH_URL,
    PluginSettings.BITBUCKET_CLIENT_AUTH_URL,
    PluginSettings.BOX_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM_CLIENT_AUTH_URL,
    PluginSettings.GOOGLE_CLIENT_TOKEN_URL,
    PluginSettings.GLOBUS_CLIENT_TOKEN_URL,
    PluginSettings.GITHUB_CLIENT_TOKEN_URL,
    PluginSettings.LINKEDIN_CLIENT_TOKEN_URL,
    PluginSettings.BITBUCKET_CLIENT_TOKEN_URL,
    PluginSettings.BOX_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM_CLIENT_TOKEN_URL,
    PluginSettings.GOOGLE_CLIENT_SCOPE,
    PluginSettings.GLOBUS_CLIENT_SCOPE,
    PluginSettings.GITHUB_CLIENT_SCOPE,
    PluginSettings.LINKEDIN_CLIENT_SCOPE,
    PluginSettings.BITBUCKET_CLIENT_SCOPE,
    PluginSettings.BOX_CLIENT_SCOPE,
    PluginSettings.CUSTOM_CLIENT_SCOPE
})
def _defaultOtherSettings():
    return ''


@setting_utilities.validator(PluginSettings.PROVIDERS_ENABLED)
def _validateProvidersEnabled(doc):
    if not isinstance(doc['value'], (list, tuple)):
        raise ValidationException('The enabled providers must be a list.', 'value')


@setting_utilities.validator(PluginSettings.IGNORE_REGISTRATION_POLICY)
def _validateIgnoreRegistrationPolicy(doc):
    if not isinstance(doc['value'], bool):
        raise ValidationException('Ignore registration policy setting must be boolean.', 'value')


@setting_utilities.validator({
    PluginSettings.GOOGLE_CLIENT_ID,
    PluginSettings.GLOBUS_CLIENT_ID,
    PluginSettings.GITHUB_CLIENT_ID,
    PluginSettings.LINKEDIN_CLIENT_ID,
    PluginSettings.BITBUCKET_CLIENT_ID,
    PluginSettings.BOX_CLIENT_ID,
    PluginSettings.CUSTOM_CLIENT_ID,
    PluginSettings.GOOGLE_CLIENT_SECRET,
    PluginSettings.GLOBUS_CLIENT_SECRET,
    PluginSettings.GITHUB_CLIENT_SECRET,
    PluginSettings.LINKEDIN_CLIENT_SECRET,
    PluginSettings.BITBUCKET_CLIENT_SECRET,
    PluginSettings.BOX_CLIENT_SECRET,
    PluginSettings.CUSTOM_CLIENT_SECRET,
    PluginSettings.GOOGLE_CLIENT_AUTH_URL,
    PluginSettings.GLOBUS_CLIENT_AUTH_URL,
    PluginSettings.GITHUB_CLIENT_AUTH_URL,
    PluginSettings.LINKEDIN_CLIENT_AUTH_URL,
    PluginSettings.BITBUCKET_CLIENT_AUTH_URL,
    PluginSettings.BOX_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM_CLIENT_AUTH_URL,
    PluginSettings.GOOGLE_CLIENT_TOKEN_URL,
    PluginSettings.GLOBUS_CLIENT_TOKEN_URL,
    PluginSettings.GITHUB_CLIENT_TOKEN_URL,
    PluginSettings.LINKEDIN_CLIENT_TOKEN_URL,
    PluginSettings.BITBUCKET_CLIENT_TOKEN_URL,
    PluginSettings.BOX_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM_CLIENT_TOKEN_URL,
    PluginSettings.GOOGLE_CLIENT_SCOPE,
    PluginSettings.GLOBUS_CLIENT_SCOPE,
    PluginSettings.GITHUB_CLIENT_SCOPE,
    PluginSettings.LINKEDIN_CLIENT_SCOPE,
    PluginSettings.BITBUCKET_CLIENT_SCOPE,
    PluginSettings.BOX_CLIENT_SCOPE,
    PluginSettings.CUSTOM_CLIENT_SCOPE
})
def _validateOtherSettings(doc):
    pass
