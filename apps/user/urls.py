from django.urls import path

from .views import LoginAPIView, RegisterAPIView, SavedItemCreateAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path("login/", LoginAPIView.as_view(), name="user-login"),
    path("saved-item/create/", SavedItemCreateAPIView.as_view(), name="user-login"),
]
