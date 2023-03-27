from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user.models import User
from helpers.models import BaseModel


class Article(BaseModel):
    """Maqolalar uchun model"""

    title = models.CharField(_("Sarlavhasi"), max_length=250)
    slug = models.SlugField(_("Slugi"), max_length=250)
    slider = models.ImageField(_("Rasm"), upload_to="blog/blog/slider/")
    content = RichTextUploadingField(verbose_name=_("Maqola matni"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Maqola")
        verbose_name_plural = _("Maqolalar")


class Views(BaseModel):
    """Ko`rishlar soni"""

    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name=_("Maqola"))
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Foydalanuvchi"))
    device_id = models.CharField(_("Qurilma manzili"), max_length=250, null=True, blank=True)

    def __str__(self):
        return self.article_id.title

    class Meta:
        verbose_name = _("Ko`rishlar soni")
        verbose_name_plural = _("Ko`rishlar soni")
