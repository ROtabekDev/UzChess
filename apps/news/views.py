from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Article, Views
from .serializers import ArticleDetailSerializer, ArticleListSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = (AllowAny,)


class ArticleRetrieveAPIView(RetrieveAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
    lookup_field = "slug"
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if self.request.user.is_authenticated:
            Views.objects.update_or_create(
                article_id=instance,
                user_id=self.request.user,
            )
        elif self.request.META.get("HTTP_USER_AGENT", ""):
            device_id = self.request.META.get("HTTP_USER_AGENT", "")

            Views.objects.update_or_create(
                article_id=instance,
                device_id=device_id,
            )

        serializer = self.get_serializer(instance)

        return Response(serializer.data)
