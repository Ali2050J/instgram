from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')
    list_display_links = ('user', 'post')
