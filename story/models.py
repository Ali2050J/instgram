from django.contrib.auth.models import User
from django.db import models

from datetime import datetime


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    image = models.ImageField(upload_to='static/images/')
    caption = models.TextField(blank=True, null=True)
    like = models.ManyToManyField(User, related_name="likes", blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user.username
