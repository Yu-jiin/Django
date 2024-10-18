# Generated by Django 4.2.16 on 2024-10-18 06:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0003_comment_parent_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='like_users',
            field=models.ManyToManyField(related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
