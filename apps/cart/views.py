from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Cart
from .serializers import (CartDetailSerializer, CartItemCreateSerializer,
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


class CartDetailAPIView(RetrieveAPIView):
    serializer_class = CartDetailSerializer

    def get_queryset(self):
        return Cart.objects.filter(user_id=self.request.user, in_order=False)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj
