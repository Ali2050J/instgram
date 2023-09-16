from django import template

from accounts.models import Relation
from post.models import Save

register = template.Library()


@register.filter()
def from_user(from_user):
    return from_user


@register.filter()
def is_following(from_user, to_user):
    relation = Relation.objects.filter(from_user=from_user, to_user=to_user)
    if relation.exists():
        return True
    return False


@register.filter()
def filter_save_with_user(saves, user):
    save_post = saves.filter(user=user)
    return save_post
