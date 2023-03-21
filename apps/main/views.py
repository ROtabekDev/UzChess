from rest_framework.generics import CreateAPIView

from .serializers import ContactSerializer, ReviewCreateSerializer


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer


class ReviewsCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
