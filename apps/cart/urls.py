from django.urls import path

from .views import (CartItemCreateAPIView, CartItemDeleteFromCartAPIView,
                    ChangeCartItemQTYAPIView)

urlpatterns = [
    path("cart-item/create/", CartItemCreateAPIView.as_view()),
    path("cart-item/change-qty/", ChangeCartItemQTYAPIView.as_view()),
    path("cart-item/delete/from-cart/", CartItemDeleteFromCartAPIView.as_view()),
]
