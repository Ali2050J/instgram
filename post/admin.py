from django.contrib import admin

from post.models import Post, Favorite


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'status')
    raw_id_fields = ("user",)


admin.site.register(Favorite)
