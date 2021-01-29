
import contextlib
from rest_framework_simplejwt.tokens import RefreshToken


@contextlib.contextmanager
def authenticate_client(client, user):
    token = RefreshToken.for_user(user)
    client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token.access_token}"

    yield client

    del client.defaults["HTTP_AUTHORIZATION"]