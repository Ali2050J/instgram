from django import template

from accounts.models import Relation

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
