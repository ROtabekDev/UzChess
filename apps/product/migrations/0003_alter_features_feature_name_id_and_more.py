# Generated by Django 4.1.7 on 2023-03-23 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_discount_price_product_is_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='feature_name_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.featurename', verbose_name='Xususiyat nomi'),
        ),
        migrations.AlterField(
            model_name='features',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Mahsulot'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Mahsulot'),
        ),
    ]
