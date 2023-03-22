from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from apps.main.models import Reviews
from helpers.models import BaseModel


class Product(BaseModel):
    """Mahsulotlar uchun model"""

    title = models.CharField("Nomi", max_length=150)
    slug = models.SlugField("Slugi", max_length=150)
    description = models.TextField("Tavsifi")
    price = models.DecimalField("Narxi", max_digits=12, decimal_places=2, default=0)
    reviews = GenericRelation(Reviews)
    qty = models.PositiveIntegerField("Mahsulotlar soni", default=0)
    available = models.BooleanField("Mavjudligi", default=False)
    is_discount = models.BooleanField("Chegirma", default=False)
    discount_price = models.DecimalField("Chegirmadagi narxi", max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class Features(BaseModel):
    """Mahsulot xususiyatlari uchun model"""

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature_name_id = models.ForeignKey("FeatureName", on_delete=models.CASCADE)
    value = models.CharField("Qiymati", max_length=150)

    def __str__(self):
        return f"{self.product_id.title} | {self.feature_name_id.title} | {self.value}"

    class Meta:
        verbose_name = "Mahsulot xususiyati"
        verbose_name_plural = "Mahsulot xususiyatlari"


class FeatureName(BaseModel):
    """Xususiyat nomlari uchun model"""

    title = models.CharField("Nomi", max_length=150)
    slug = models.SlugField("Slugi", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xususiyat nomi"
        verbose_name_plural = "Xususiyat nomlari"


class ProductImages(BaseModel):
    """Mahsulot rasmlarini saqlovchi model"""

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField("Rasmi", upload_to="product/product-images/image/")
    use_in_slider = models.BooleanField("Slider uchun", default=False)

    def __str__(self):
        return self.product_id.title

    class Meta:
        verbose_name = "Mahsulot rasmi"
        verbose_name_plural = "Mahsulot rasmlari"


class PurchasedProduct(BaseModel):
    """Sotib olingan mahsulotlar"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Kurs")
    qty = models.PositiveIntegerField("Mahsulotlar soni")

    def __str__(self):
        return f"User: {self.user_id.phone_number}. Mahsulot: {self.book_id.title}"

    class Meta:
        verbose_name = "Sotib olingan mahsulot"
        verbose_name_plural = "Sotib olingan mahsulotlar"
