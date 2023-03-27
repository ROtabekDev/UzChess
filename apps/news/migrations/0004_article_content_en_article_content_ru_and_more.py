# Generated by Django 4.1.7 on 2023-03-27 04:48

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_content_alter_views_article_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Maqola matni'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Maqola matni'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Maqola matni'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Sarlavhasi'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Sarlavhasi'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Sarlavhasi'),
        ),
    ]
