from django.contrib import admin

from .models import Article, Views

 
@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    prepopulated_fields = {"slug": ("title",)} 
    list_display_links = ('title',) 


@admin.register(Views)
class ViewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_id', 'user_id', 'device_id')
    list_display_links = ('article_id', 'user_id') 