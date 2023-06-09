# Generated by Django 4.1.7 on 2023-03-23 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0005_alter_episode_length_alter_episode_section_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('file', models.FileField(blank=True, null=True, upload_to='education/certificate/file/', verbose_name='Fayl')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course', verbose_name='Kurs')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Sertifikat',
                'verbose_name_plural': 'Sertifikatlar',
            },
        ),
    ]
