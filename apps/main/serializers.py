from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Reviews


class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ("user_id", "rate_number", "message")
