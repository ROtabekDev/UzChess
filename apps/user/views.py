from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from .models import SavedItem
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


class SavedItemDeleteAPIView(DestroyAPIView):
    def get_object(self):
        ct_model = self.kwargs.get("ct_model")
        object_slug = self.kwargs.get("object_slug")

        try:
            content_type = ContentType.objects.get(model=ct_model)
            product = content_type.model_class().objects.get(slug=object_slug)
        except:
            raise Http404

        user = self.request.user

        saved_item = get_object_or_404(SavedItem, user_id=user, content_type=content_type, object_id=product.id)

        return saved_item
