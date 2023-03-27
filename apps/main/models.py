from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from helpers.models import BaseModel


class Reviews(BaseModel):
    """Kurslar, kitoblar va mahsulotlar uchun foydalanuvchi
    tomonidan qoldirilga izohlar uchun model.
    Masalan, Shaxmat kursi uchun 5 baho, kurs alo darajada"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_("Model"))
    object_id = models.PositiveIntegerField(verbose_name=_("Obyekt id"))
    content_object = GenericForeignKey("content_type", "object_id")
    rate_number = models.PositiveIntegerField(
        _("Reyting qiymati"), validators=[MinValueValidator(0), MaxValueValidator(5)], default=0
    )
    message = models.CharField(_("Xabar"), max_length=250)

    def __str__(self):
        return f"{self.rate_number} {self.message}"

    class Meta:
        verbose_name = _("Izoh")
        verbose_name_plural = _("Izohlar")


class Contact(BaseModel):
    """Foydalanuvchi tomonidan yuboriladigan xabarlar uchun model"""

    first_name = models.CharField(_("Ism"), max_length=150)
    phone_number = PhoneNumberField(_("Telefon nomer"), max_length=32, unique=True)
    message = models.TextField(_("Xabar"))

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _("Xabar")
        verbose_name_plural = _("Xabarlar")


class Leval(BaseModel):
    """Kurs va kitoblar uchun qiyinchilik darajalari uchun model.
    Masalan, boshlang`ich, o`rta va yuqori"""

    name = models.CharField(_("Nomi"), max_length=150)
    slug = models.SlugField(_("Slugi"), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Daraja")
        verbose_name_plural = _("Darajalar")


class Author(BaseModel):
    """Kurs va kitobning muallifi uchun model.
    Masalan, Magnus Carlsen"""

    first_name = models.CharField(_("Ismi"), max_length=150)
    last_name = models.CharField(_("Familiyasi"), max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Muallif")
        verbose_name_plural = _("Mualliflar")


class Language(BaseModel):
    """Kurs va kitoblar qaysi tilda ekanligini saqlab borish uchun model.
    Masalan, O`zbek tili, Rus tili va Ingliz tili"""

    name = models.CharField(_("Nomi"), max_length=150)
    slug = models.SlugField(_("Slugi"), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Til")
        verbose_name_plural = _("Tillar")
