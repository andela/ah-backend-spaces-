# Generated by Django 2.0.6 on 2018-08-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='read_status',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
