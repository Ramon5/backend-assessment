import pytest

from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse

from tests.factories import UserFactory, RequestFactory
from tests.authentication import authenticate_client

pytestmark = pytest.mark.django_db


class TestRequestsQueryView:

    client = APIClient()

    def test_should_return_403_when_retrieve_requests_without_authentication(self):
        response = self.client.get(reverse("requests"))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_should_return_200_when_retrieve_requests_successfully(self):
        user = UserFactory.create()

        RequestFactory.create(owner=user)

        with authenticate_client(self.client, user) as client:
            client.force_authenticate(user=user)
            response = client.get(reverse("requests"), format="json")

        assert response.status_code == status.HTTP_200_OK
        assert user.id in [entry['owner'] for entry in response.json()]

    def test_commom_user_access_only_owner_requests(self):
        primary_user = UserFactory.create()
        secondary_user = UserFactory.create()

        primary_user_requests = [
            RequestFactory.create(owner=primary_user),
            RequestFactory.create(owner=primary_user),
        ]

        RequestFactory.create(owner=secondary_user),
        RequestFactory.create(owner=secondary_user),

        with authenticate_client(self.client, primary_user) as client:
            client.force_authenticate(user=primary_user)
            response = client.get(reverse("requests"), format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == len(primary_user_requests)
        assert primary_user.id in [entry['owner'] for entry in response.json()]

    def test_admin_user_can_access_all_requests_created(self):
        admin = UserFactory.create(is_superuser=True, is_staff=True)

        primary_user = UserFactory.create()
        secondary_user = UserFactory.create()

        primary_user_requests = [
            RequestFactory.create(owner=primary_user),
            RequestFactory.create(owner=primary_user),
        ]

        secondary_user_requests = [
            RequestFactory.create(owner=secondary_user),
            RequestFactory.create(owner=secondary_user),
        ]

        with authenticate_client(self.client, admin) as client:
            client.force_authenticate(user=admin)
            response = client.get(reverse("requests"), format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == len(
            primary_user_requests + secondary_user_requests
        )