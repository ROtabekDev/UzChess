from django.urls import path

from .views import ProductListAPIView

urlpatterns = [path("list/", ProductListAPIView.as_view())]
