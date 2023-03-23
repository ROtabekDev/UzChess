from django.urls import path

from .views import (LoginAPIView, RegisterAPIView, SavedItemCreateAPIView,
                    SavedItemDeleteAPIView, SavedItemListAPIView,
                    UserUpdateAPIView)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path("login/", LoginAPIView.as_view(), name="user-login"),
    path("update/", UserUpdateAPIView.as_view()),
    path("saved-item/create/", SavedItemCreateAPIView.as_view()),
    path("saved-item/delete/<str:ct_model>/<str:object_slug>/", SavedItemDeleteAPIView.as_view()),
    path("saved-item/list/", SavedItemListAPIView.as_view()),
]
