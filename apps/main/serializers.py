from django.contrib.contenttypes.models import ContentType
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


class ReviewCreateSerializer(serializers.ModelSerializer):
    ct_model = serializers.CharField(write_only=True)
    object_slug = serializers.SlugField(write_only=True)

    class Meta:
        model = Reviews
        fields = ("ct_model", "object_slug", "rate_number", "message")

    def create(self, validated_data):
        content_type = ContentType.objects.get(model=validated_data["ct_model"])

        product = content_type.model_class().objects.get(slug=validated_data["object_slug"])

        user = self.context["request"].user

        review = Reviews.objects.get_or_create(user_id=user, content_type=content_type, object_id=product.id)

        review[0].rate_number = validated_data["rate_number"]
        review[0].message = validated_data["message"]
        review[0].save()

        return review[0]
