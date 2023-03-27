from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from helpers.models import BaseModel


class CustomUserManager(BaseUserManager):
    """Maxsus foydalanuvchi menejeri"""

    def create_user(self, first_name, last_name, phone_number, password=None):
        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, phone_number, password=None):
        user = self.model(
            phone_number=phone_number, first_name=first_name, last_name=last_name, password=make_password(password)
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """Foydalanuvchi uchun model"""

    first_name = models.CharField(_("Ism"), max_length=100)
    last_name = models.CharField(_("Familiya"), max_length=100)
    phone_number = PhoneNumberField(_("Telefon nomer"), max_length=32, unique=True)
    email = models.EmailField(_("Elektron pochta"), unique=True, blank=True, null=True)
    avatar = models.ImageField(
        _("Sahifa uchun rasm"), upload_to="user/user/avatar/", default="user/user/avatar/default-user.png"
    )
    birthday = models.DateField(_("Tug`ilgan sanasi"), null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Foydalanuvchi")
        verbose_name_plural = _("Barcha foydalanuvchilar")

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class SavedItem(BaseModel):
    """Saqlab qo`yilgan narsalar uchun model"""

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_("Model"))
    object_id = models.PositiveIntegerField(_("Obyekt id"))
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f"{self.user_id.first_name} {self.content_object}"

    class Meta:
        verbose_name = _("Saqlagan narsa")
        verbose_name_plural = _("Saqlagan narsalar")
