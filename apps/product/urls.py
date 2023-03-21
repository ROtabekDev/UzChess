from django.urls import path

from .views import ProductDetailAPIView, ProductListAPIView

urlpatterns = [
    path("list/", ProductListAPIView.as_view()),
    path("detail/<str:slug>/", ProductDetailAPIView.as_view()),
]
