import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.authentication import authenticate_client
from tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserView:

    client = APIClient()
    url = reverse("register")

    def test_should_return_201_when_created_user_successfully(self):
        payload = {
            "username": "test",
            "email": "test@test.com",
            "password": "test12345678",
            "password2": "test12345678",
            "first_name": "fulano",
            "last_name": "de tal",
        }

        response = self.client.post(self.url, data=payload, format="json")

        assert response.status_code == status.HTTP_201_CREATED

    def test_should_return_400_when_register_new_user_without_required_param(self):
        payload = {
            "username": "test",
            "password": "test12345678",
            "password2": "test12345678",
            "first_name": "fulano",
            "last_name": "de tal",
        }

        response = self.client.post(self.url, data=payload, format="json")

        response.status_code == status.HTTP_400_BAD_REQUEST

    def test_should_return_200_when_logged_successfully(self):
        user = UserFactory.create(username="testuser")
        user.set_password("test123")
        user.save()

        payload = {"username": user.username, "password": "test123"}

        response = self.client.post(
            reverse("token_obtain_pair"), data=payload, format="json"
        )

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.json()
        assert "refresh" in response.json()

    def test_should_return_400_when_not_pass_required_param_in_login(self):
        user = UserFactory.create(username="testuser")
        user.set_password("test123")
        user.save()

        payload = {"username": user.username}

        response = self.client.post(
            reverse("token_obtain_pair"), data=payload, format="json"
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
