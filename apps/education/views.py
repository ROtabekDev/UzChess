from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Book
from .serializers import BookDetailSerializer, BookListSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ("title",)
    filterset_fields = ("leval_id", "author_id", "language_id")


class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = "slug"
