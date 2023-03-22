from rest_framework.generics import CreateAPIView

from .serializers import CartItemCreateSerializer, ChangeCartItemQTYSerializer


class CartItemCreateAPIView(CreateAPIView):
    serializer_class = CartItemCreateSerializer


class ChangeCartItemQTYAPIView(CreateAPIView):
    serializer_class = ChangeCartItemQTYSerializer
