# Generated by Django 4.1.7 on 2023-03-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_alter_section_section_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=False, verbose_name='Mavjudligi'),
        ),
    ]