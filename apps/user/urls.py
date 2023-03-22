from django.urls import path

from .views import (LoginAPIView, RegisterAPIView, SavedItemCreateAPIView,
                    SavedItemDeleteAPIView)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path("login/", LoginAPIView.as_view(), name="user-login"),
    path("saved-item/create/", SavedItemCreateAPIView.as_view(), name="user-login"),
    path("saved-item/delete/<str:ct_model>/<str:object_slug>/", SavedItemDeleteAPIView.as_view(), name="user-login"),
]
