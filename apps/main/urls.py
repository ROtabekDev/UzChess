from django.urls import path

from .views import ContactCreateAPIView, ReviewsCreateAPIView

urlpatterns = [
    path("create/contact/", ContactCreateAPIView.as_view()),
    path("create/review/", ReviewsCreateAPIView.as_view()),
]
