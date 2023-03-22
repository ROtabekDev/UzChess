from django.contrib import admin

from .models import (Cart, CartItem, CartProduct, District, Order, PaymentType,
                     Region)


@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "cart", "content_object", "qty", "final_price")
    list_display_links = ("id", "user_id", "cart", "content_object")
    list_filter = ("user_id", "cart")


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "total_products", "in_order")
    list_display_links = (
        "id",
        "user_id",
    )
    list_filter = ("user_id",)


@admin.register(CartProduct)
class CartProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "cart_id", "product_id")
    list_display_links = ("id", "cart_id", "product_id")
    list_filter = ("cart_id",)


@admin.register(Order)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "first_name", "last_name", "phone_number")
    list_display_links = ("id", "user_id", "first_name")
    list_filter = ("user_id",)


@admin.register(Region)
class RegionModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("title",)


@admin.register(District)
class DistrictModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("title",)


@admin.register(PaymentType)
class PaymentTypeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("title",)
