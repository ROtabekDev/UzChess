from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import (LoginSerializer, RegisterSerializer,
                          SavedItemCreateSerializer)


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        pass


class SavedItemCreateAPIView(CreateAPIView):
    serializer_class = SavedItemCreateSerializer
