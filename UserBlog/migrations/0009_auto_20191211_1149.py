# Generated by Django 2.2 on 2019-12-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserBlog', '0008_auto_20191211_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/'),
        ),
    ]
