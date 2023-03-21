from django.urls import path

from .views import ContactCreateAPIView

urlpatterns = [path("create/contact/", ContactCreateAPIView.as_view())]
