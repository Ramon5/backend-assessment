from django.contrib.auth.models import User
from rest_framework import serializers

from .constants import StatusRequest
from .models import ActivationRequest


class ActivationRequestDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    status = serializers.ChoiceField(choices=StatusRequest.CHOICES)
    created_at = serializers.DateTimeField(read_only=True)


class ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivationRequest
        fields = "__all__"
