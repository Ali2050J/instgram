from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('users/', view=views.UserListView.as_view(), name='user_list'),
    path('posts/', view=views.PostListView.as_view(), name='post_list'),
    path('posts/<str:username>/', view=views.UserPostListView.as_view(), name='user_post_list'),
    path('favorite-posts/<str:username>/', view=views.UserFavoritePostListView.as_view(), name='user_favorite_post_list'),
    path('<str:username>/followers/', view=views.UserFollowerListView.as_view(), name='user_follower_list'),
    path('<str:username>/followings/', view=views.UserFollowingListView.as_view(), name='user_following_list'),
]
