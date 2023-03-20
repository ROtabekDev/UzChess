# Generated by Django 4.1.7 on 2023-03-20 13:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_saveditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=32, region=None, unique=True, verbose_name='Telefon nomer'),
        ),
    ]
