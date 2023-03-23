from django.contrib import admin

from .models import (Book, CategoryForCourse, CompletedCourse, Course, Episode,
                     EpisodeViewed, PurchasedBook, PurchasedCourse, Section, Certificate)


@admin.register(CategoryForCourse)
class CategoryForCourseModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("title",)


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author_id", "category_id", "leval_id")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("title", "author_id")
    list_filter = ("author_id", "category_id", "leval_id")


@admin.register(Section)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "section_type", "is_public")
    list_display_links = ("id", "title", "section_type")
    list_filter = ("section_type",)


@admin.register(Episode)
class EpisodeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "section_id")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("id", "title")
    list_filter = ("section_id",)


@admin.register(EpisodeViewed)
class EpisodeViewedModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "episode_id")
    list_display_links = ("user_id", "episode_id")
    list_filter = ("user_id",)


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author_id", "leval_id", "total_pages")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("title", "author_id")
    list_filter = ("author_id", "leval_id")


@admin.register(PurchasedCourse)
class PurchasedCourseViewedModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "course_id")
    list_display_links = ("user_id", "course_id")
    list_filter = ("user_id",)


@admin.register(CompletedCourse)
class CompletedCourseViewedModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "course_id")
    list_display_links = ("user_id", "course_id")
    list_filter = ("user_id",)


@admin.register(PurchasedBook)
class PurchasedBookViewedModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "book_id", "qty")
    list_display_links = ("user_id", "book_id")
    list_filter = ("user_id",)


@admin.register(Certificate)
class CertificateModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "course_id")
    list_display_links = ("user_id", "course_id")
    list_filter = ("user_id",)