# Generated by Django 5.1 on 2024-09-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_main_image_post_thumbnail_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='Images/mainimage/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='Images/thumbnails/'),
        ),
    ]
