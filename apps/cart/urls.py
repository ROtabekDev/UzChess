from django.urls import path

from .views import CartItemCreateAPIView, ChangeCartItemQTYAPIView

urlpatterns = [
    path("cart-item/create/", CartItemCreateAPIView.as_view()),
    path("cart-item/change-qty/", ChangeCartItemQTYAPIView.as_view()),
]
