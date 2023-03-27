import random

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from helpers.models import BaseModel


class CartItem(BaseModel):
    """Savatdagi mahsulotlar uchun"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    cart = models.ForeignKey("Cart", verbose_name=_("Savat"), on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_("Mahsulot turi"))
    object_id = models.PositiveIntegerField(verbose_name=_("Mahsulot id"))
    content_object = GenericForeignKey("content_type", "object_id")
    qty = models.PositiveIntegerField(_("Mahsulotlar soni"), default=1)
    final_price = models.DecimalField(_("Jami summa"), max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if self.content_object.is_discount:
            self.final_price = self.qty * self.content_object.discount_price
        else:
            self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.content_object.title

    class Meta:
        verbose_name = _("Savatdagi mahsulot")
        verbose_name_plural = _("Savatdagi mahsulotlar")


class Cart(BaseModel):
    """Saval uchun model"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    total_products = models.IntegerField(default=0, verbose_name=_("Jami mahsulotlar soni"))
    final_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Jami summa"), default=0)
    discout_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Chegirma summasi"), default=0)
    discount_percentage = models.PositiveIntegerField(_("Chegirma foizi"), default=0)
    shipping_cost = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name=("Yetkazib berish narxi"), default=0
    )
    in_order = models.BooleanField(_("Buyurtma qiliganligi"), default=False)

    def __str__(self):
        return f"{self.user_id.first_name} {self.user_id.last_name}"

    class Meta:
        verbose_name = _("Savat")
        verbose_name_plural = _("Savatlar")


class CartProduct(BaseModel):
    """Qaysi savatga qaysi mahsulot tegishli
    ekanligini saqlab borish uchun model"""

    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_("Savat"))
    product_id = models.ForeignKey(CartItem, on_delete=models.CASCADE, verbose_name=_("Mahsulot"))

    def __str__(self):
        return f"{self.cart_id.user_id.first_name} {self.cart_id.user_id.last_name}"

    class Meta:
        verbose_name = _("Savatga tegishli mahsulot")
        verbose_name_plural = _("Savatga tegishli mahsulotlar")


class BuyigType(models.TextChoices):
    Self = "Self", "O`zim olib ketaman"
    Delivery = "Delivery", "Yetkazib berish"


class OrderStatus(models.TextChoices):
    New = "New", _("Yangi")
    In_progress = "In_progress", _("Jarayoda")
    Error = "Error", _("Xatolik")
    Completed = "Completed", _("Bajarildi")


class Order(BaseModel):
    """Buyurtmalar uchun model"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_("Savat"))
    first_name = models.CharField(_("Ismi"), max_length=150)
    last_name = models.CharField(_("Familiya"), max_length=150)
    phone_number = PhoneNumberField(_("Telefon nomer"), max_length=32)
    buying_type = models.CharField(_("Yetkazib berish turi"), choices=BuyigType.choices, max_length=20)
    region_id = models.ForeignKey("Region", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Viloyat"))
    district_id = models.ForeignKey(
        "District", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Tuman")
    )
    home_address = models.CharField("Uy manzili", max_length=250)
    text = models.TextField(_("Xabar"))
    payment_type = models.ForeignKey(
        "PaymentType", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("To`lov turi")
    )
    order_number = models.PositiveBigIntegerField(_("Buyurtma raqami"), unique=True)
    status = models.CharField(_("Buyurtma holati"), choices=OrderStatus.choices, max_length=20, default="In_progress")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"

    def save(self, *args, **kwargs):
        while True:
            order_number = "".join([str(random.randint(1, 9)) for _ in range(12)])

            if not Order.objects.filter(order_number=int(order_number)).exists():
                order_number = int(order_number)
                self.order_number = order_number
                break
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")


class Region(BaseModel):
    """Viloyatlar uchun model"""

    title = models.CharField(_("Nomi"), max_length=50)
    slug = models.SlugField(_("Slugi"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Viloyat")
        verbose_name_plural = _("Viloyatlar")


class District(BaseModel):
    """Tumanlar uchun model"""

    title = models.CharField(_("Nomi"), max_length=50)
    slug = models.SlugField(_("Slugi"), max_length=50)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_("Viloyat"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Tuman")
        verbose_name_plural = _("Tumanlar")


class PaymentType(BaseModel):
    """To`lov usullari uchun model"""

    title = models.CharField(_("Nomi"), max_length=50)
    slug = models.SlugField(_("Slugi"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("To`lov usuli")
        verbose_name_plural = _("To`lov usullari")
