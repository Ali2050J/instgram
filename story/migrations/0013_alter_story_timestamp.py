# Generated by Django 4.2.4 on 2023-09-17 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0012_alter_story_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 20, 45, 28, 490363)),
        ),
    ]