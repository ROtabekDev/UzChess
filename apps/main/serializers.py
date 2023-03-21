from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Contact, Reviews


class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ("user_id", "rate_number", "message")


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ("first_name", "phone_number", "message")
