# Generated by Django 4.1.7 on 2023-03-27 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_features_feature_name_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurename',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='featurename',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='featurename',
            name='title_uz',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Tavsifi'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Tavsifi'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Tavsifi'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
    ]