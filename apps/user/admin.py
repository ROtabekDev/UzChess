from django.contrib import admin

from .models import SavedItem, User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number")
    list_display_links = ("id", "first_name", "last_name")


@admin.register(SavedItem)
class SavedItemModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "content_type", "object_id")
    list_display_links = ("id", "user_id")
    list_filter = ("user_id",)
