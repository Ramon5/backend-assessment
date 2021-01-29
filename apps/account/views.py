from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class UserView(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, **kwargs):
        queryset = self.get_queryset()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        qs = User.objects.all()
        if not self.request.user.is_superuser:
            qs = qs.filter(id=self.request.user.id)
        return qs
