from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Product
from .serializers import ProductDetailSerializer, ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("title",)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "slug"
