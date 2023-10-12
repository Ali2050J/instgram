from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    GENDERS = (
        ('Femail', 'femail'),
        ('Mail', 'mail'),
        ('Prefer not to say', 'prefer not to say'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='../static/images/defaut_user.webp')
    full_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDERS, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('accounts:user_profile', args=(self.user.id, ))

    def __str__(self):
        return f'{self.full_name}'


class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followings')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'
