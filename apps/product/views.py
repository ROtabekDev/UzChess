from rest_framework import filters
from rest_framework.generics import ListAPIView

from .models import Product
from .serizlizers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("title",)
