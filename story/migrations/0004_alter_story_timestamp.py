# Generated by Django 4.2.4 on 2023-09-15 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_alter_story_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 15, 10, 12, 17, 48112)),
        ),
    ]