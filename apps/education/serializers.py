from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.main.models import Reviews
from apps.main.serializers import ReviewsSerializer

from .models import Book


class BookListSerializer(ModelSerializer):
    author_id = serializers.StringRelatedField()
    leval_id = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = (
            "title",
            "slug",
            "author_id",
            "leval_id",
            "total_pages",
            "slider",
            "price",
            "is_discount",
            "discount_price",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation["is_discount"] == False:
            del representation["is_discount"]
            del representation["discount_price"]

        content_type = ContentType.objects.get(model="book")
        book = content_type.model_class().objects.get(slug=representation["slug"])

        count_ranking = Reviews.objects.filter(content_type=content_type, object_id=book.id).count()
        sum_ranking = Reviews.objects.filter(content_type=content_type, object_id=book.id).aggregate(
            Sum("rate_number")
        )["rate_number__sum"]

        if sum_ranking == None:
            sum_ranking = 0

        try:
            ranking = sum_ranking / count_ranking
        except ZeroDivisionError:
            ranking = 0

        ranking = round(ranking, 1)

        representation["ranking"] = ranking
        representation["ct_model"] = "book"

        return representation


class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "title",
            "slug",
            "author_id",
            "leval_id",
            "language_id",
            "total_pages",
            "year_of_issue",
            "desciption",
            "slider",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        content_type = ContentType.objects.get(model="book")
        book = content_type.model_class().objects.get(slug=representation["slug"])

        count_ranking = Reviews.objects.filter(content_type=content_type, object_id=book.id).count()
        sum_ranking = Reviews.objects.filter(content_type=content_type, object_id=book.id).aggregate(
            Sum("rate_number")
        )["rate_number__sum"]

        if sum_ranking == None:
            sum_ranking = 0

        try:
            ranking = sum_ranking / count_ranking
        except ZeroDivisionError:
            ranking = 0

        ranking = round(ranking, 1)

        reviews = Reviews.objects.filter(content_type=content_type, object_id=book.id)

        if reviews.exists():
            serializer = ReviewsSerializer(reviews, many=True)
            representation["reviews"] = serializer.data

        representation["ranking"] = ranking
        representation["count_ranking"] = count_ranking
        representation["ct_model"] = "book"

        return representation
