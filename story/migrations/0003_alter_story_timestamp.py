# Generated by Django 4.2.5 on 2023-10-07 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_alter_story_image_alter_story_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 7, 18, 32, 22, 715719)),
        ),
    ]
