import factory
from factory.django import DjangoModelFactory

from django.contrib.auth.models import User
from apps.requests.models import ActivationRequest
from apps.requests.constants import StatusRequest


class UserFactory(DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user{0}'.format(n))

    class Meta:
        model = User
        django_get_or_create = ("username",)


class RequestFactory(DjangoModelFactory):

    owner = factory.SubFactory(UserFactory)
    status = StatusRequest.SUBMITTED

    class Meta:
        model = ActivationRequest