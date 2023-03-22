from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from .serializers import (CartItemCreateSerializer,
                          CartItemDeleteFromCartSerializer,
                          ChangeCartItemQTYSerializer)


class CartItemCreateAPIView(CreateAPIView):
    serializer_class = CartItemCreateSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"status": 200, "message": "Mahsulot qo`shildi."})


class ChangeCartItemQTYAPIView(CreateAPIView):
    serializer_class = ChangeCartItemQTYSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"status": 200, "message": "Muvaffaqiyatli o`zgartirildi."})


class CartItemDeleteFromCartAPIView(CreateAPIView):
    serializer_class = CartItemDeleteFromCartSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"status": 200, "message": "Mahsulot o`chirildi."})
