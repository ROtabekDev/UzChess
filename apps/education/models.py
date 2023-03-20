from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from mutagen.mp4 import MP4, MP4StreamInfoError

from apps.main.models import Author, Language, Leval, Reviews
from helpers.models import BaseModel


class CategoryForCourse(BaseModel):
    """Kurslar uchun kategoriya modeli"""

    title = models.CharField("Sarlavhasi", max_length=150)
    slug = models.SlugField("Slugi", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Course(BaseModel):
    """Kurs uchun modeli"""

    title = models.CharField("Kurs nomi", max_length=150)
    slug = models.SlugField("Slugi", max_length=150)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Muallif")
    category_id = models.ForeignKey(CategoryForCourse, on_delete=models.CASCADE, verbose_name="Kategoriya")
    leval_id = models.ForeignKey(Leval, on_delete=models.CASCADE, verbose_name="Kurs darajasi")
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tili")
    desciption = models.TextField("Kurs haqida ma`lumot")
    slider = models.ImageField("Rasm", upload_to="education/course/slider/")
    reviews = GenericRelation(Reviews)
    price = models.DecimalField("Narxi", max_digits=12, decimal_places=2, default=0)
    is_discount = models.BooleanField("Chegirma", default=False)
    discount_price = models.DecimalField("Chegirmadagi narxi", max_digits=12, decimal_places=2, default=0)
    is_free = models.BooleanField("Bepul", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class SectioType(models.TextChoices):
    Not_seen = "Not_seen", "Ko`rilmagan"
    In_progress = "In_progress", "Jarayonda"
    Reviewed = "Reviewed", "Ko`rilgan"


class Section(BaseModel):
    """Bo`limlar uchun model"""

    title = models.CharField("Sarlavhasi", max_length=150)
    order = models.PositiveIntegerField("Tartib nomeri", default=1)
    section_type = models.CharField("Bo`lim turi", choices=SectioType.choices, default="Not seen", max_length=20)
    is_public = models.BooleanField(default=False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order}. {self.title}"

    class Meta:
        verbose_name = "Bo`lim"
        verbose_name_plural = "Bo`limlar"


class Episode(BaseModel):
    """Videolar uchun model"""

    title = models.CharField("Nomi", max_length=150)
    slug = models.SlugField("Slugi", max_length=150)
    file = models.FileField("Fayl", upload_to="course/episode/file/")
    order = models.PositiveIntegerField("Tartib nomeri", default=1)
    length = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True, default=0)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)

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
        verbose_name = "Epizod"
        verbose_name_plural = "Epizodlar"


class EpisodeViewed(BaseModel):
    """Video ko`rilganligi"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    episode_id = models.ForeignKey(Episode, on_delete=models.CASCADE)

    def __str__(self):
        return self.episode_id.title

    class Meta:
        verbose_name = "Video ko`rilganligi"
        verbose_name_plural = "Video ko`rilganligi"


class Book(BaseModel):
    """Kitoblar uchun model"""

    title = models.CharField("Kitob nomi", max_length=150)
    slug = models.SlugField("Slugi", max_length=150)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Muallif")
    leval_id = models.ForeignKey(Leval, on_delete=models.CASCADE, verbose_name="Kitob darajasi")
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tili")
    total_pages = models.PositiveIntegerField("Sahifalar soni")
    year_of_issue = models.PositiveIntegerField("Ishlab chiqarilgan yili")
    desciption = models.TextField("Kitob haqida ma`lumot")
    slider = models.ImageField("Rasm", upload_to="education/book/slider/")
    reviews = GenericRelation(Reviews)
    price = models.DecimalField("Narxi", max_digits=12, decimal_places=2, default=0)
    is_discount = models.BooleanField("Chegirma", default=False)
    discount_price = models.DecimalField("Chegirmadagi narxi", max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"


class PurchasedCourse(BaseModel):
    """Sotib olingan kurslar"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Kurs")

    def __str__(self):
        return f"User: {self.user_id.phone_number}. Kurs: {self.course_id.title}"

    class Meta:
        verbose_name = "Sotib olingan kurs"
        verbose_name_plural = "Sotib olingan kurslar"


class CompletedCourse(BaseModel):
    """Tugatilgan kurslar"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Kurs")

    def __str__(self):
        return f"User: {self.user_id.phone_number}. Kurs: {self.course_id.title}"

    class Meta:
        verbose_name = "Tugatilgan kurs"
        verbose_name_plural = "Tugatilgan kurslar"


class PurchasedBook(BaseModel):
    """Sotib olingan kitoblar"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Kurs")
    qty = models.PositiveIntegerField("Kitoblar soni")

    def __str__(self):
        return f"User: {self.user_id.phone_number}. Kitob: {self.book_id.title}"

    class Meta:
        verbose_name = "Sotib olingan kitob"
        verbose_name_plural = "Sotib olingan kitoblar"
