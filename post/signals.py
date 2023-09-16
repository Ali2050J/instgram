from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Save


def create_save(sender, **kwargs):
    if kwargs['created']:
        Save.objects.create(user=kwargs['instance'])


post_save.connect(receiver=create_save, sender=User)
