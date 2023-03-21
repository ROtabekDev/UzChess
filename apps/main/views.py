from rest_framework.generics import CreateAPIView

from .models import Contact
from .serializers import ContactSerializer


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer
