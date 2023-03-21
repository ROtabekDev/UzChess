from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import FeatureName, Features, Product, ProductImages


class ProductImagesSerializer(ModelSerializer):
    product_id = serializers.StringRelatedField()

    class Meta:
        model = ProductImages
        fields = ("product_id", "image", "use_in_slider")


class FeaturesSerializer(ModelSerializer):
    product_id = serializers.StringRelatedField()
    feature_name_id = serializers.StringRelatedField()

    class Meta:
        model = Features
        fields = ("product_id", "feature_name_id", "value")


class ProductListSerializer(ModelSerializer):
    images = serializers.DictField(read_only=True)

    class Meta:
        model = Product
        fields = ("title", "price", "images")

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        images = ProductImages.objects.filter(product_id=instance)

        if images.exists():
            serializer = ProductImagesSerializer(images, many=True, context={"request": self.context["request"]})
            representation["images"] = serializer.data

        return representation
