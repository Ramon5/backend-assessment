from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.mixins import CommandRequestManager
from apps.requests.constants import StatusRequest
from apps.requests.serializers import ActivationRequestSerializer


class CommandSubmitRequestView(APIView):

    serializer_class = ActivationRequestSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        payload = request.data.copy()
        payload["owner"] = request.user.id
        payload["status"] = StatusRequest.SUBMITTED

        serializer = ActivationRequestSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class CommandRequestApproveView(CommandRequestManager):

    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ActivationRequestSerializer
    status = StatusRequest.APPROVED


class CommandRequestRejectView(CommandRequestManager):

    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ActivationRequestSerializer
    status = StatusRequest.REJECTED


class CommandRequestCancellingView(CommandRequestManager):

    serializer_class = ActivationRequestSerializer
    status = StatusRequest.CANCELED
