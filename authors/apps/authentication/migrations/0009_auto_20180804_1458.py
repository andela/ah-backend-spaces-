# Generated by Django 2.0.6 on 2018-08-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20180804_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='social_id',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
