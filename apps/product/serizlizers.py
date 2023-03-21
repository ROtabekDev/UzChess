from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.main.models import Reviews
from apps.main.serializers import ReviewsSerializer

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
        fields = ("title", "slug", "price", "images")

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        images = ProductImages.objects.filter(product_id=instance)

        if images.exists():
            serializer = ProductImagesSerializer(images, many=True, context={"request": self.context["request"]})
            representation["images"] = serializer.data

        return representation


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "slug", "description")

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        content_type = ContentType.objects.get(model="product")
        product = content_type.model_class().objects.get(slug=representation["slug"])
        print(content_type)
        print(product)

        count_ranking = Reviews.objects.filter(content_type=content_type, object_id=product.id).count()
        sum_ranking = Reviews.objects.filter(content_type=content_type, object_id=product.id).aggregate(
            Sum("rate_number")
        )["rate_number__sum"]

        if sum_ranking == None:
            sum_ranking = 0

        try:
            ranking = sum_ranking / count_ranking
        except ZeroDivisionError:
            ranking = 0

        ranking = round(ranking, 1)

        reviews = Reviews.objects.filter(content_type=content_type, object_id=product.id)

        print(reviews)
        if reviews.exists():
            serializer = ReviewsSerializer(reviews, many=True)
            representation["reviews"] = serializer.data

        representation["ranking"] = ranking
        representation["count_ranking"] = count_ranking

        return representation
