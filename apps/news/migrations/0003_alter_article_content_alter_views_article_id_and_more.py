# Generated by Django 4.1.7 on 2023-03-23 06:14

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Maqola matni'),
        ),
        migrations.AlterField(
            model_name='views',
            name='article_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.article', verbose_name='Maqola'),
        ),
        migrations.AlterField(
            model_name='views',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
    ]