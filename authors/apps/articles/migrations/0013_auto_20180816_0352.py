# Generated by Django 2.0.6 on 2018-08-16 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_article_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user_id',
            new_name='author',
        ),
    ]
