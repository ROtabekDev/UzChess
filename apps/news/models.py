from django.db import models

from helpers.models import BaseModel

from apps.user.models import User


class Article(BaseModel):
    """Maqolalar uchun model"""
    title = models.CharField('Sarlavhasi', max_length=250)
    slug = models.SlugField('Slugi', max_length=250)   
    slider = models.ImageField('Rasm', upload_to='blog/blog/slider/')
    content = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Views(BaseModel):
    """Ko`rishlar soni"""
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    device_id = models.CharField('Qurilma manzili', max_length=250, null=True, blank=True) 

    def __str__(self):
        return self.article_id.title
    
    class Meta:
        verbose_name = 'Ko`rishlar soni'
        verbose_name_plural = 'Ko`rishlar soni'