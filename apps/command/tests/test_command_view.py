import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken, Token

from apps.command.views import CommandSubmitRequestView
from apps.requests.constants import StatusRequest
from tests.authentication import authenticate_client
from tests.factories import RequestFactory, UserFactory

pytestmark = pytest.mark.django_db


class TestSubmitCommandView:

    client = APIClient()
    url = reverse("api-submit-request")

    def test_should_return_401_when_submit_request_without_authentication(self):
        response = self.client.post(self.url)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_should_return_201_when_request_submitted_successfully(self):
        user = UserFactory.create()

        with authenticate_client(self.client, user) as client:
            client.force_authenticate(user=user)
            response = client.post(self.url)

        assert response.status_code == status.HTTP_201_CREATED
