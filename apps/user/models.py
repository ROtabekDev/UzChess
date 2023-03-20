from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
from django.db import models
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

    first_name = models.CharField("Ism", max_length=100)
    last_name = models.CharField("Familiya", max_length=100)
    phone_number = PhoneNumberField("Telefon nomer", max_length=32, unique=True)
    email = models.EmailField("Elektron pochta", unique=True, blank=True, null=True)
    avatar = models.ImageField(
        "Sahifa uchun rasm", upload_to="user/user/avatar/", default="user/user/avatar/default-user.png"
    )
    birthday = models.DateField("Tug`ilgan sanasi", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Barcha foydalanuvchilar"

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class SavedItem(BaseModel):
    """Saqlab qo`yilgan narsalar uchun model"""

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.user_id.phone_number

    class Meta:
        verbose_name = "Saqlagan narsa"
        verbose_name_plural = "Saqlagan narsalar"
