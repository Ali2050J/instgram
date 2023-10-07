from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('posts/', view=views.PostListView.as_view(), name='post_list'),
    path('favorite-posts/', view=views.FavoritePostListView.as_view(), name='favorite_post_list'),
]
