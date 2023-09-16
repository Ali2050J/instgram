from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    STATUS = (
        ('publish', 'publish'),
        ('draft', 'draft'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='static/images/')
    caption = models.TextField()
    like = models.ManyToManyField(User, related_name="liked", blank=True, default=None)
    status = models.CharField(max_length=20, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.caption[:10]}...'


class Save(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saves')
    post = models.ManyToManyField(Post, related_name='save', blank=True, null=True)

    def __str__(self):
        return f'{self.user}'