from django.urls import path

from .views import BookListAPIView

urlpatterns = [path("book/list/", BookListAPIView.as_view())]
