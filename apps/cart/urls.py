from django.urls import path

from .views import (CartDetailAPIView, CartItemCreateAPIView,
                    CartItemDeleteFromCartAPIView, ChangeCartItemQTYAPIView,
                    DistrictListAPIView, OrderCreateAPIView, OrderListAPIView,
                    PaymentTypeListAPIView, RegionListAPIView)

urlpatterns = [
    path("detail/", CartDetailAPIView.as_view()),
    path("cart-item/create/", CartItemCreateAPIView.as_view()),
    path("cart-item/change-qty/", ChangeCartItemQTYAPIView.as_view()),
    path("cart-item/delete/from-cart/", CartItemDeleteFromCartAPIView.as_view()),
    path("order/create/", OrderCreateAPIView.as_view()),
    path("order/list/", OrderListAPIView.as_view()),
    path("region/list/", RegionListAPIView.as_view()),
    path("district/list/", DistrictListAPIView.as_view()),
    path("payment-type/list/", PaymentTypeListAPIView.as_view()),
]
