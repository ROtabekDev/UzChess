# Generated by Django 4.1.7 on 2023-03-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'Yangi'), ('In_progress', 'Jarayoda'), ('Error', 'Xatolik'), ('Completed', 'Bajarildi')], max_length=20, verbose_name='Buyurtma holati'),
        ),
    ]