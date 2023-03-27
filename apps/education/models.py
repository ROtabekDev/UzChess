from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _
from mutagen.mp4 import MP4, MP4StreamInfoError

from apps.main.models import Author, Language, Leval, Reviews
from helpers.models import BaseModel


class CategoryForCourse(BaseModel):
    """Kurslar uchun kategoriya modeli"""

    title = models.CharField(_("Sarlavhasi"), max_length=150)
    slug = models.SlugField(_("Slugi"), max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")


class Course(BaseModel):
    """Kurs uchun modeli"""

    title = models.CharField(_("Kurs nomi"), max_length=150)
    slug = models.SlugField(_("Slugi"), max_length=150)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_("Muallif"))
    category_id = models.ForeignKey(CategoryForCourse, on_delete=models.CASCADE, verbose_name=_("Kategoriya"))
    leval_id = models.ForeignKey(Leval, on_delete=models.CASCADE, verbose_name=_("Kurs darajasi"))
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name=_("Tili"))
    desciption = models.TextField(_("Kurs haqida ma`lumot"))
    slider = models.ImageField(_("Rasm"), upload_to="education/course/slider/")
    reviews = GenericRelation(Reviews)
    price = models.DecimalField(_("Narxi"), max_digits=12, decimal_places=2, default=0)
    is_discount = models.BooleanField(_("Chegirma"), default=False)
    discount_price = models.DecimalField(_("Chegirmadagi narxi"), max_digits=12, decimal_places=2, default=0)
    is_free = models.BooleanField(_("Bepul"), default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Kurs")
        verbose_name_plural = _("Kurslar")


class SectioType(models.TextChoices):
    Not_seen = "Not_seen", _("Ko`rilmagan")
    In_progress = "In_progress", _("Jarayonda")
    Reviewed = "Reviewed", _("Ko`rilgan")


class Section(BaseModel):
    """Bo`limlar uchun model"""

    title = models.CharField(_("Sarlavhasi"), max_length=150)
    order = models.PositiveIntegerField(_("Tartib nomeri"), default=1)
    section_type = models.CharField(_("Bo`lim turi"), choices=SectioType.choices, default="Not seen", max_length=20)
    is_public = models.BooleanField(_("Hamma uchun"), default=False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Kurs"))

    def __str__(self):
        return f"{self.order}. {self.title}"

    class Meta:
        verbose_name = _("Bo`lim")
        verbose_name_plural = _("Bo`limlar")


class Episode(BaseModel):
    """Videolar uchun model"""

    title = models.CharField(_("Nomi"), max_length=150)
    slug = models.SlugField(_("Slugi"), max_length=150)
    file = models.FileField(_("Fayl"), upload_to="course/episode/file/")
    order = models.PositiveIntegerField(_("Tartib nomeri"), default=1)
    length = models.DecimalField(
        _("Video davomiyligi"), max_digits=100, decimal_places=2, blank=True, null=True, default=0
    )
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Bo`lim"))

    def get_video_length(self):
        try:
            video = MP4(self.file)
            return video.info.length

        except MP4StreamInfoError:
            return 0.0

    def save(self, *args, **kwargs):
        self.length = self.get_video_length()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Epizod")
        verbose_name_plural = _("Epizodlar")


class EpisodeViewed(BaseModel):
    """Video ko`rilganligi"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    episode_id = models.ForeignKey(Episode, on_delete=models.CASCADE, verbose_name=_("Video"))

    def __str__(self):
        return self.episode_id.title

    class Meta:
        verbose_name = _("Video ko`rilganligi")
        verbose_name_plural = _("Video ko`rilganligi")


class Book(BaseModel):
    """Kitoblar uchun model"""

    title = models.CharField(_("Kitob nomi"), max_length=150)
    slug = models.SlugField(_("Slugi"), max_length=150)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_("Muallif"))
    leval_id = models.ForeignKey(Leval, on_delete=models.CASCADE, verbose_name=_("Kitob darajasi"))
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name=_("Tili"))
    total_pages = models.PositiveIntegerField(_("Sahifalar soni"))
    year_of_issue = models.PositiveIntegerField(_("Ishlab chiqarilgan yili"))
    desciption = models.TextField(_("Kitob haqida ma`lumot"))
    slider = models.ImageField(_("Rasm"), upload_to="education/book/slider/")
    reviews = GenericRelation(Reviews)
    price = models.DecimalField(_("Narxi"), max_digits=12, decimal_places=2, default=0)
    available = models.BooleanField(_("Mavjudligi"), default=False)
    is_discount = models.BooleanField(_("Chegirma"), default=False)
    discount_price = models.DecimalField(_("Chegirmadagi narxi"), max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Kitob")
        verbose_name_plural = _("Kitoblar")


class PurchasedCourse(BaseModel):
    """Sotib olingan kurslar"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Kurs"))

    def __str__(self):
        return f"User: {self.user_id.phone_number}. Kurs: {self.course_id.title}"

    class Meta:
        verbose_name = _("Sotib olingan kurs")
        verbose_name_plural = _("Sotib olingan kurslar")


class CompletedCourse(BaseModel):
    """Tugatilgan kurslar"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Kurs"))

    def __str__(self):
        return f"User: {self.user_id.phone_number}. Kurs: {self.course_id.title}"

    class Meta:
        verbose_name = _("Tugatilgan kurs")
        verbose_name_plural = _("Tugatilgan kurslar")


class PurchasedBook(BaseModel):
    """Sotib olingan kitoblar"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_("Kurs"))
    qty = models.PositiveIntegerField(_("Kitoblar soni"))

    def __str__(self):
        return f"User: {self.user_id.phone_number}. Kitob: {self.book_id.title}"

    class Meta:
        verbose_name = _("Sotib olingan kitob")
        verbose_name_plural = _("Sotib olingan kitoblar")


class Certificate(BaseModel):
    """Sertifikat uchun model"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Kurs"))
    file = models.FileField(_("Fayl"), blank=True, null=True, upload_to="education/certificate/file/")

    def __str__(self):
        return f"{self.user_id.first_name} + {self.user_id.first_name}"

    class Meta:
        verbose_name = _("Sertifikat")
        verbose_name_plural = _("Sertifikatlar")
