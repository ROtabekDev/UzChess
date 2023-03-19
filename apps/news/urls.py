from django.urls import path

from .views import (
    ArticleListAPIView, ArticleRetrieveAPIView
)

urlpatterns = [ 
    path('list/', ArticleListAPIView.as_view()),
    path('detail/<str:slug>/', ArticleRetrieveAPIView.as_view()),
]