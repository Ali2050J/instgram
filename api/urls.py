from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('users/', view=views.UserListView.as_view(), name='user_list'),
    path('posts/', view=views.PostListView.as_view(), name='post_list'),

    path('posts/<str:username>/', view=views.UserPostListView.as_view(), name='user_post_list'),
    path('favorite-posts/<str:username>/', view=views.UserFavoritePostListView.as_view(), name='user_favorite_post_list'),
    path('post/likes/<int:post_id>/', view=views.PostLikeListView.as_view(), name='post_likes'),
    path('followers/<str:username>/', view=views.UserFollowerListView.as_view(), name='user_follower_list'),
    path('followings/<str:username>/', view=views.UserFollowingListView.as_view(), name='user_following_list'),

    path('favorite/add/', view=views.AddFavoriteView.as_view(), name='add_favorite'),
    path('post/like/add/', view=views.AddLikeView.as_view(), name='add_like'),
]
