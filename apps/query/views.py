from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.requests.models import ActivationRequest
from apps.requests.serializers import ActivationRequestDetailSerializer


class QueryActivationRequestsView(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ActivationRequestDetailSerializer

    def get(self, request, **kwargs):
        qs = self.get_queryset()

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        qs = ActivationRequest.objects.select_related("owner").all()
        if not self.request.user.is_superuser:
            qs = qs.filter(owner=self.request.user)
        return qs


class QueryActivationRequestsDetail(APIView):

    serializer_class = ActivationRequestDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        activation_request = get_object_or_404(ActivationRequest, id=id)

        if not request.user.is_superuser:
            activation_request = get_object_or_404(
                ActivationRequest, id=id, owner=request.user
            )

        serializer = self.serializer_class(activation_request)

        return Response(serializer.data, status=status.HTTP_200_OK)
