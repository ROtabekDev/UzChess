from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Cart, District, PaymentType, Region
from .serializers import (CartDetailSerializer, CartItemCreateSerializer,
                          CartItemDeleteFromCartSerializer,
                          ChangeCartItemQTYSerializer, DistrictListSerializer,
                          OrderCreateSerializer, PaymentTypeListSerializer,
                          RegionListSerializer)


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


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictListSerializer


class PaymentTypeListAPIView(ListAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeListSerializer
