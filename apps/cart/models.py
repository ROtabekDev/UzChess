from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from helpers.models import BaseModel


class CartItem(BaseModel):
    """Savatdagi mahsulotlar uchun"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    cart = models.ForeignKey("Cart", verbose_name="Savat", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Jami summa")

    def __str__(self):
        return self.content_object.title

    class Meta:
        verbose_name = "Savatdagi mahsulot"
        verbose_name_plural = "Savatdagi mahsulotlar"


class Cart(BaseModel):
    """Saval uchun model"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    total_products = models.IntegerField(default=0, verbose_name="Jami mahsulotlar soni")
    final_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Jami summa", null=True, blank=True)
    discout_price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Chegirma summasi", null=True, blank=True
    )
    discount_percentage = models.PositiveIntegerField("Chegirma foizi", null=True, blank=True)
    shipping_cost = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Yetkazib berish narxi", null=True, blank=True
    )
    in_order = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.phone_number

    class Meta:
        verbose_name = "Savat"
        verbose_name_plural = "Savatlar"


class CartProduct(BaseModel):
    """Qaysi savatga qaysi mahsulot tegishli
    ekanligini saqlab borish uchun model"""

    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Savatdagi mahsulot"
        verbose_name_plural = "Savatdagi mahsulotlar"


class BuyigType(models.TextChoices):
    Self = "Self", "O`zim olib ketaman"
    Delivery = "Delivery", "Yetkazib berish"


class OrderStatus(models.TextChoices):
    New = "New", "Yangi"
    In_progress = "In_progress", "Jarayoda"
    Error = "Error", "Xatolik"
    Completed = "Completed", "Bajarildi"


class Order(BaseModel):
    """Buyurtmalar uchun model"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    first_name = models.CharField("Ismi", max_length=150)
    last_name = models.CharField("Familiya", max_length=150)
    phone_number = PhoneNumberField("Telefon nomer", max_length=32)
    buying_type = models.CharField("Yetkazib berish turi", choices=BuyigType.choices, max_length=20)
    region_id = models.ForeignKey("Region", on_delete=models.SET_NULL, null=True, blank=True)
    district_id = models.ForeignKey("District", on_delete=models.SET_NULL, null=True, blank=True)
    home_address = models.CharField("Uy manzili", max_length=250)
    text = models.TextField("Xabar")
    payment_type = models.ForeignKey("PaymentType", on_delete=models.SET_NULL, null=True, blank=True)
    order_number = models.PositiveBigIntegerField("Buyurtma raqami", unique=True)
    status = models.CharField("Buyurtma holati", choices=OrderStatus.choices, max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


class Region(BaseModel):
    """Viloyatlar uchun model"""

    title = models.CharField("Nomi", max_length=50)
    slug = models.SlugField("Slugi", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"


class District(BaseModel):
    """Tumanlar uchun model"""

    title = models.CharField("Nomi", max_length=50)
    slug = models.SlugField("Slugi", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"


class PaymentType(BaseModel):
    """To`lov usullari uchun model"""

    title = models.CharField("Nomi", max_length=50)
    slug = models.SlugField("Slugi", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "To`lov usuli"
        verbose_name_plural = "To`lov usullari"
