# Generated by Django 4.2.5 on 2023-10-11 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_alter_story_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 11, 11, 57, 33, 927177)),
        ),
    ]
