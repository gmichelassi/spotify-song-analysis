from config import SPOTIFY_AUTH_URL
from config import SPOTIFY_SCOPE_PERMISSIONS as SCOPE
from errors import MissingEnvironmentVariableError

import os


def get_authentication_query_params(redirect_uri: str) -> dict:
    try:
        return {
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "scope": SCOPE,
            "client_id": os.environ["SPOTIFY_CLIENT_ID"],
        }
    except KeyError:
        raise MissingEnvironmentVariableError("SPOTIFY_CLIENT_ID")


def get_authentication_url(url_args: str) -> str:
    return f"{SPOTIFY_AUTH_URL}/?{url_args}"
