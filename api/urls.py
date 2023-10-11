from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    # register - login - logout
    path('register/', view=views.RegisterView.as_view(), name='auth_register'),
    path('login/', view=views.user_login, name='login'),
    path('logout/', view=views.user_logout, name='logout'),

    # users - user posts
    path('users/', view=views.UserListView.as_view(), name='user_list'),
    path('user_posts/<str:username>/', view=views.UserPostListView.as_view(), name='user_post_list'),
    
    # followers - followings
    path('user_followers/<str:username>/', view=views.UserFollowerListView.as_view(), name='user_follower_list'),
    path('user_followings/<str:username>/', view=views.UserFollowingListView.as_view(), name='user_following_list'),
    
    path('follow/add/', view=views.AddFollowView.as_view(), name='add_follow'),
    path('follow/<str:to_user>/delete/<str:from_user>/', view=views.DeleteFollowView.as_view(), name='delete_follow'),

    
    # user favorites
    path('user_favorite-posts/<str:username>/', view=views.UserFavoritePostListView.as_view(), name='user_favorite_post_list'),
    path('favorite/add/', view=views.AddFavoriteView.as_view(), name='add_favorite'),
    path('favorite/<str:username>/delete/<int:post_id>/', view=views.DeleteFavoriteView.as_view(), name='delete_favorite'),
    
    # posts - post's like
    path('posts/', view=views.PostListView.as_view(), name='post_list'),
    path('post/likes/<int:post_id>/', view=views.PostLikeListView.as_view(), name='post_likes'),
    path('post/like/add/', view=views.AddLikeView.as_view(), name='add_like'),
    path('post/<int:post_id>/like/delete/<str:username>/', view=views.DeleteLikeView.as_view(), name='delete_like'),


]
