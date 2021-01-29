from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.command.tasks import approve_request, reject_request
from apps.requests.constants import StatusRequest
from apps.requests.models import ActivationRequest
from apps.requests.serializers import ActivationRequestSerializer

MAPPING_CALL_TASK = {
    "approved": approve_request,
    "rejected": reject_request,
    "canceled": None,
}


class CommandRequestManager(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = None
    status = None

    def post(self, request, id):
        payload = request.data.copy()

        payload["status"] = self.status

        activation_request = get_object_or_404(
            ActivationRequest, id=id, owner__id=payload["owner"]
        )

        serializer = ActivationRequestSerializer(
            activation_request, data=payload
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        task = MAPPING_CALL_TASK[self.status]
        task.delay(activation_request.owner.email) if task else None

        return Response(status=status.HTTP_200_OK)

    patch = post
    put = post
