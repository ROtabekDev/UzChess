from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Article, Views


class ArticleListSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "slug", "slider", "content", "created_at")


class ArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "slider", "content", "created_at")

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        view_count = Views.objects.filter(article_id=instance).count()

        representation["view_count"] = view_count

        return representation
