# Generated by Django 5.1 on 2024-09-03 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='author_email',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='author',
            new_name='author_email',
        ),
    ]
