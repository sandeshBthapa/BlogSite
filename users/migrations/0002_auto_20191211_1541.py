# Generated by Django 2.2 on 2019-12-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='profile_pic'),
        ),
    ]
