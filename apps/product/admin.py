from django.contrib import admin

from .models import (FeatureName, Features, Product, ProductImages,
                     PurchasedProduct)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "available")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = (
        "id",
        "title",
    )


@admin.register(Features)
class FeaturesModelAdmin(admin.ModelAdmin):
    list_display = ("id", "product_id", "feature_name_id", "value")
    list_display_links = ("id", "product_id", "feature_name_id")
    list_filter = ("product_id",)


@admin.register(FeatureName)
class FeatureNameModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = (
        "id",
        "title",
    )


@admin.register(ProductImages)
class ProductImagesModelAdmin(admin.ModelAdmin):
    list_display = ("id", "product_id", "image", "use_in_slider")
    list_display_links = (
        "id",
        "product_id",
    )
    list_filter = ("product_id",)


@admin.register(PurchasedProduct)
class PurchasedProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "product_id", "qty")
    list_display_links = ("id", "user_id", "product_id")
    list_filter = ("user_id",)
