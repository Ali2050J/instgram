# Generated by Django 4.0.2 on 2023-09-19 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0013_alter_story_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 19, 18, 56, 42, 876090)),
        ),
    ]
