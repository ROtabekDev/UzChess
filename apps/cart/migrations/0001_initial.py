# Generated by Django 4.1.7 on 2023-03-20 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('total_products', models.IntegerField(default=0, verbose_name='Jami mahsulotlar soni')),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Jami summa')),
                ('discout_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Chegirma summasi')),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True, verbose_name='Chegirma foizi')),
                ('shipping_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Yetkazib berish narxi')),
                ('in_order', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Savat',
                'verbose_name_plural': 'Savatlar',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Jami summa')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Savat')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Savatdagi mahsulot',
                'verbose_name_plural': 'Savatdagi mahsulotlar',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
                ('slug', models.SlugField(verbose_name='Slugi')),
            ],
            options={
                'verbose_name': 'Tuman',
                'verbose_name_plural': 'Tumanlar',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
                ('slug', models.SlugField(verbose_name='Slugi')),
            ],
            options={
                'verbose_name': 'To`lov usuli',
                'verbose_name_plural': 'To`lov usullari',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
                ('slug', models.SlugField(verbose_name='Slugi')),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('first_name', models.CharField(max_length=150, verbose_name='Ismi')),
                ('last_name', models.CharField(max_length=150, verbose_name='Familiya')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefo raqam')),
                ('buying_type', models.CharField(choices=[('Self', 'O`zim olib ketaman'), ('Delivery', 'Yetkazib berish')], max_length=20, verbose_name='Yetkazib berish turi')),
                ('home_address', models.CharField(max_length=250, verbose_name='Uy manzili')),
                ('text', models.TextField(verbose_name='Xabar')),
                ('order_number', models.PositiveBigIntegerField(unique=True, verbose_name='Buyurtma raqami')),
                ('status', models.CharField(choices=[], max_length=20, verbose_name='Buyurtma holati')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('district_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.district')),
                ('payment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.paymenttype')),
                ('region_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.region')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartitem')),
            ],
            options={
                'verbose_name': 'Savatdagi mahsulot',
                'verbose_name_plural': 'Savatdagi mahsulotlar',
            },
        ),
    ]
