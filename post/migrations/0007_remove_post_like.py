# Generated by Django 4.2.4 on 2023-09-17 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]