# Generated by Django 4.2.5 on 2023-10-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../static/images/defaut_user.webp', null=True, upload_to='images/'),
        ),
    ]