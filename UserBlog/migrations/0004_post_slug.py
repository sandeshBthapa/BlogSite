# Generated by Django 2.2 on 2019-12-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserBlog', '0003_remove_comment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Slug',
            field=models.SlugField(default=True, max_length=100, unique=True),
        ),
    ]
