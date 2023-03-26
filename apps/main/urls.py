from django.urls import path

from .views import (ContactCreateAPIView, GetPlayersRating, GoogleLogin,
                    ReviewsCreateAPIView)

urlpatterns = [
    path("create/contact/", ContactCreateAPIView.as_view()),
    path("create/review/", ReviewsCreateAPIView.as_view()),
    path("get-players-rating/", GetPlayersRating.as_view()),
    path("google-login/", GoogleLogin.as_view()),
]
