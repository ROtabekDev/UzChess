from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.main.models import Reviews
from helpers.models import BaseModel


class Product(BaseModel):
    """Mahsulotlar uchun model"""

    title = models.CharField(_("Nomi"), max_length=150)
    slug = models.SlugField(_("Slugi"), max_length=150)
    description = models.TextField(_("Tavsifi"))
    price = models.DecimalField(_("Narxi"), max_digits=12, decimal_places=2, default=0)
    reviews = GenericRelation(Reviews)
    qty = models.PositiveIntegerField(_("Mahsulotlar soni"), default=0)
    available = models.BooleanField(_("Mavjudligi"), default=False)
    is_discount = models.BooleanField(_("Chegirma"), default=False)
    discount_price = models.DecimalField(_("Chegirmadagi narxi"), max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Mahsulot")
        verbose_name_plural = _("Mahsulotlar")


class Features(BaseModel):
    """Mahsulot xususiyatlari uchun model"""

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Mahsulot"))
    feature_name_id = models.ForeignKey("FeatureName", on_delete=models.CASCADE, verbose_name=_("Xususiyat nomi"))
    value = models.CharField(_("Qiymati"), max_length=150)

    def __str__(self):
        return f"{self.product_id.title} | {self.feature_name_id.title} | {self.value}"

    class Meta:
        verbose_name = _("Mahsulot xususiyati")
        verbose_name_plural = _("Mahsulot xususiyatlari")


class FeatureName(BaseModel):
    """Xususiyat nomlari uchun model"""

    title = models.CharField(_("Nomi"), max_length=150)
    slug = models.SlugField(_("Slugi"), max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Xususiyat nomi")
        verbose_name_plural = _("Xususiyat nomlari")


class ProductImages(BaseModel):
    """Mahsulot rasmlarini saqlovchi model"""

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Mahsulot"))
    image = models.ImageField(_("Rasmi"), upload_to="product/product-images/image/")
    use_in_slider = models.BooleanField(_("Slider uchun"), default=False)

    def __str__(self):
        return self.product_id.title

    class Meta:
        verbose_name = _("Mahsulot rasmi")
        verbose_name_plural = _("Mahsulot rasmlari")


class PurchasedProduct(BaseModel):
    """Sotib olingan mahsulotlar"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Kurs"))
    qty = models.PositiveIntegerField(_("Mahsulotlar soni"))

    def __str__(self):
        return f"User: {self.user_id.phone_number}. Mahsulot: {self.book_id.title}"

    class Meta:
        verbose_name = _("Sotib olingan mahsulot")
        verbose_name_plural = _("Sotib olingan mahsulotlar")
