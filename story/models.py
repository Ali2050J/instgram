from django.contrib.auth.models import User
from django.db import models


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(blank=True, null=True)
    like = models.ManyToManyField(User, related_name="likes", blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
