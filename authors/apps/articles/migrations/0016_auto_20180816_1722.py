# Generated by Django 2.0.6 on 2018-08-16 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_merge_20180816_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlefavourites',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='articlelikes',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='user_id',
            new_name='author',
        ),
    ]
