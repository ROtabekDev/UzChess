from django.db import models

from apps.cart.models import CartItem


def update_cart(user, cart):
    cart_data = CartItem.objects.filter(user_id=user, cart=cart).aggregate(models.Sum("final_price"), models.Sum("qty"))

    if cart_data.get("final_price__sum"):
        cart.final_price = cart_data["final_price__sum"]
    else:
        cart.final_price = 0
    if cart_data.get("qty__sum"):
        cart.total_products = cart_data["qty__sum"]
    else:
        cart.total_products = 0
    cart.save()
