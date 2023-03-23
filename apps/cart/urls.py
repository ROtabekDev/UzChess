from django.urls import path

from .views import (CartDetailAPIView, CartItemCreateAPIView,
                    CartItemDeleteFromCartAPIView, ChangeCartItemQTYAPIView)

urlpatterns = [
    path("cart-item/create/", CartItemCreateAPIView.as_view()),
    path("cart-item/change-qty/", ChangeCartItemQTYAPIView.as_view()),
    path("cart-item/delete/from-cart/", CartItemDeleteFromCartAPIView.as_view()),
    path("detail/", CartDetailAPIView.as_view()),
]
