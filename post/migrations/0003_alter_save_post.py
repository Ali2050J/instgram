# Generated by Django 4.2.4 on 2023-09-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_save'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, related_name='save', to='post.post'),
        ),
    ]