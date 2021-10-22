from girder.exceptions import ValidationException
from girder.utility import setting_utilities


class PluginSettings:
    PROVIDERS_ENABLED = 'oauth.providers_enabled'
    IGNORE_REGISTRATION_POLICY = 'oauth.ignore_registration_policy'

    GOOGLE_CLIENT_ID = 'oauth.google_client_id'
    GOOGLE_CLIENT_SECRET = 'oauth.google_client_secret'

    GLOBUS_CLIENT_ID = 'oauth.globus_client_id'
    GLOBUS_CLIENT_SECRET = 'oauth.globus_client_secret'

    GITHUB_CLIENT_ID = 'oauth.github_client_id'
    GITHUB_CLIENT_SECRET = 'oauth.github_client_secret'

    LINKEDIN_CLIENT_ID = 'oauth.linkedin_client_id'
    LINKEDIN_CLIENT_SECRET = 'oauth.linkedin_client_secret'

    BITBUCKET_CLIENT_ID = 'oauth.bitbucket_client_id'
    BITBUCKET_CLIENT_SECRET = 'oauth.bitbucket_client_secret'

    BOX_CLIENT_ID = 'oauth.box_client_id'
    BOX_CLIENT_SECRET = 'oauth.box_client_secret'

    CUSTOM_CLIENT_ID = 'oauth.custom_client_id'
    CUSTOM_CLIENT_SECRET = 'oauth.custom_client_secret'
    CUSTOM_CLIENT_AUTH_URL = 'oauth.custom_client_auth_url'
    CUSTOM_CLIENT_TOKEN_URL = 'oauth.custom_client_token_url'
    CUSTOM_CLIENT_SCOPE = 'oauth.custom_client_scope'
    CUSTOM_CLIENT_BUTTON_COLOR = "oauth.custom_client_button_color"
    CUSTOM_CLIENT_ICON_URL = 'oauth.custom_client_icon_url'
    CUSTOM_CLIENT_NAME = 'oauth.custom_client_name'

    CUSTOM2_CLIENT_ID = 'oauth.custom2_client_id'
    CUSTOM2_CLIENT_SECRET = 'oauth.custom2_client_secret'
    CUSTOM2_CLIENT_AUTH_URL = 'oauth.custom2_client_auth_url'
    CUSTOM2_CLIENT_TOKEN_URL = 'oauth.custom2_client_token_url'
    CUSTOM2_CLIENT_SCOPE = 'oauth.custom2_client_scope'
    CUSTOM2_CLIENT_BUTTON_COLOR = "oauth.custom2_client_button_color"
    CUSTOM2_CLIENT_ICON_URL = 'oauth.custom2_client_icon_url'
    CUSTOM2_CLIENT_NAME = 'oauth.custom2_client_name'

    CUSTOM3_CLIENT_ID = 'oauth.custom3_client_id'
    CUSTOM3_CLIENT_SECRET = 'oauth.custom3_client_secret'
    CUSTOM3_CLIENT_AUTH_URL = 'oauth.custom3_client_auth_url'
    CUSTOM3_CLIENT_TOKEN_URL = 'oauth.custom3_client_token_url'
    CUSTOM3_CLIENT_SCOPE = 'oauth.custom3_client_scope'
    CUSTOM3_CLIENT_BUTTON_COLOR = "oauth.custom3_client_button_color"
    CUSTOM3_CLIENT_ICON_URL = 'oauth.custom3_client_icon_url'
    CUSTOM3_CLIENT_NAME = 'oauth.custom3_client_name'

    CUSTOM4_CLIENT_ID = 'oauth.custom4_client_id'
    CUSTOM4_CLIENT_SECRET = 'oauth.custom4_client_secret'
    CUSTOM4_CLIENT_AUTH_URL = 'oauth.custom4_client_auth_url'
    CUSTOM4_CLIENT_TOKEN_URL = 'oauth.custom4_client_token_url'
    CUSTOM4_CLIENT_SCOPE = 'oauth.custom4_client_scope'
    CUSTOM4_CLIENT_BUTTON_COLOR = "oauth.custom4_client_button_color"
    CUSTOM4_CLIENT_ICON_URL = 'oauth.custom4_client_icon_url'
    CUSTOM4_CLIENT_NAME = 'oauth.custom4_client_name'

    CUSTOM5_CLIENT_ID = 'oauth.custom5_client_id'
    CUSTOM5_CLIENT_SECRET = 'oauth.custom5_client_secret'
    CUSTOM5_CLIENT_AUTH_URL = 'oauth.custom5_client_auth_url'
    CUSTOM5_CLIENT_TOKEN_URL = 'oauth.custom5_client_token_url'
    CUSTOM5_CLIENT_SCOPE = 'oauth.custom5_client_scope'
    CUSTOM5_CLIENT_BUTTON_COLOR = "oauth.custom5_client_button_color"
    CUSTOM5_CLIENT_ICON_URL = 'oauth.custom5_client_icon_url'
    CUSTOM5_CLIENT_NAME = 'oauth.custom5_client_name'







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
    PluginSettings.GOOGLE_CLIENT_SECRET,
    PluginSettings.GLOBUS_CLIENT_SECRET,
    PluginSettings.GITHUB_CLIENT_SECRET,
    PluginSettings.LINKEDIN_CLIENT_SECRET,
    PluginSettings.BITBUCKET_CLIENT_SECRET,
    PluginSettings.BOX_CLIENT_SECRET,
    # Custom client 1
    PluginSettings.CUSTOM_CLIENT_ID,
    PluginSettings.CUSTOM_CLIENT_SECRET,
    PluginSettings.CUSTOM_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM_CLIENT_SCOPE,
    PluginSettings.CUSTOM_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM_CLIENT_ICON_URL,
    PluginSettings.CUSTOM_CLIENT_NAME,
    # Custom client 2
    PluginSettings.CUSTOM2_CLIENT_ID,
    PluginSettings.CUSTOM2_CLIENT_SECRET,
    PluginSettings.CUSTOM2_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM2_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM2_CLIENT_SCOPE,
    PluginSettings.CUSTOM2_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM2_CLIENT_ICON_URL,
    PluginSettings.CUSTOM2_CLIENT_NAME,
    # Custom client 3
    PluginSettings.CUSTOM3_CLIENT_ID,
    PluginSettings.CUSTOM3_CLIENT_SECRET,
    PluginSettings.CUSTOM3_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM3_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM3_CLIENT_SCOPE,
    PluginSettings.CUSTOM3_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM3_CLIENT_ICON_URL,
    PluginSettings.CUSTOM3_CLIENT_NAME,
    # Custom client 4
    PluginSettings.CUSTOM4_CLIENT_ID,
    PluginSettings.CUSTOM4_CLIENT_SECRET,
    PluginSettings.CUSTOM4_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM4_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM4_CLIENT_SCOPE,
    PluginSettings.CUSTOM4_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM4_CLIENT_ICON_URL,
    PluginSettings.CUSTOM4_CLIENT_NAME,
    # Custom client 5
    PluginSettings.CUSTOM5_CLIENT_ID,
    PluginSettings.CUSTOM5_CLIENT_SECRET,
    PluginSettings.CUSTOM5_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM5_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM5_CLIENT_SCOPE,
    PluginSettings.CUSTOM5_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM5_CLIENT_ICON_URL,
    PluginSettings.CUSTOM5_CLIENT_NAME,

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
    PluginSettings.GOOGLE_CLIENT_SECRET,
    PluginSettings.GLOBUS_CLIENT_SECRET,
    PluginSettings.GITHUB_CLIENT_SECRET,
    PluginSettings.LINKEDIN_CLIENT_SECRET,
    PluginSettings.BITBUCKET_CLIENT_SECRET,
    PluginSettings.BOX_CLIENT_SECRET,
    # Custom client 1
    PluginSettings.CUSTOM_CLIENT_ID,
    PluginSettings.CUSTOM_CLIENT_SECRET,
    PluginSettings.CUSTOM_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM_CLIENT_SCOPE,
    PluginSettings.CUSTOM_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM_CLIENT_ICON_URL,
    PluginSettings.CUSTOM_CLIENT_NAME,
    # Custom client 2
    PluginSettings.CUSTOM2_CLIENT_ID,
    PluginSettings.CUSTOM2_CLIENT_SECRET,
    PluginSettings.CUSTOM2_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM2_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM2_CLIENT_SCOPE,
    PluginSettings.CUSTOM2_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM2_CLIENT_ICON_URL,
    PluginSettings.CUSTOM2_CLIENT_NAME,
    # Custom client 3
    PluginSettings.CUSTOM3_CLIENT_ID,
    PluginSettings.CUSTOM3_CLIENT_SECRET,
    PluginSettings.CUSTOM3_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM3_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM3_CLIENT_SCOPE,
    PluginSettings.CUSTOM3_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM3_CLIENT_ICON_URL,
    PluginSettings.CUSTOM3_CLIENT_NAME,
    # Custom client 4
    PluginSettings.CUSTOM4_CLIENT_ID,
    PluginSettings.CUSTOM4_CLIENT_SECRET,
    PluginSettings.CUSTOM4_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM4_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM4_CLIENT_SCOPE,
    PluginSettings.CUSTOM4_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM4_CLIENT_ICON_URL,
    PluginSettings.CUSTOM4_CLIENT_NAME,
    # Custom client 5
    PluginSettings.CUSTOM5_CLIENT_ID,
    PluginSettings.CUSTOM5_CLIENT_SECRET,
    PluginSettings.CUSTOM5_CLIENT_AUTH_URL,
    PluginSettings.CUSTOM5_CLIENT_TOKEN_URL,
    PluginSettings.CUSTOM5_CLIENT_SCOPE,
    PluginSettings.CUSTOM5_CLIENT_BUTTON_COLOR,
    PluginSettings.CUSTOM5_CLIENT_ICON_URL,
    PluginSettings.CUSTOM5_CLIENT_NAME,
})
def _validateOtherSettings(doc):
    pass
