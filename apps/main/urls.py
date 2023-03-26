from django.urls import path

from .views import ContactCreateAPIView, GetPlayersRating, ReviewsCreateAPIView

urlpatterns = [
    path("create/contact/", ContactCreateAPIView.as_view()),
    path("create/review/", ReviewsCreateAPIView.as_view()),
    path("get-players-rating/", GetPlayersRating.as_view()),
]
