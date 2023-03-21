from django.urls import path

from .views import BookDetailAPIView, BookListAPIView

urlpatterns = [
    path("book/list/", BookListAPIView.as_view()),
    path("book/detail/<str:slug>/", BookDetailAPIView.as_view()),
]
