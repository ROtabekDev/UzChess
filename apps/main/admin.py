from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Author, Contact, Language, Leval, Reviews


@admin.register(Reviews)
class ReviewsModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "content_object", "rate_number")
    list_display_links = ("user_id", "content_object")


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "phone_number")
    list_display_links = ("first_name", "phone_number")


@admin.register(Leval)
class LevalModelAdmin(TranslationAdmin):
    list_display = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = (
        "id",
        "name",
    )


@admin.register(Author)
class AuthorModelAdmin(TranslationAdmin):
    list_display = ("id", "first_name", "last_name")
    list_display_links = ("first_name", "last_name")


@admin.register(Language)
class LanguageModelAdmin(TranslationAdmin):
    list_display = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = (
        "id",
        "name",
    )
