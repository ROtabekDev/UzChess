# Generated by Django 4.1.7 on 2023-03-20 10:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Episode_viewed',
            new_name='EpisodeViewed',
        ),
    ]
