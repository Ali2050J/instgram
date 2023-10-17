from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    # register - login - logout
    path('register/', view=views.RegisterView.as_view(), name='auth_register'),
    path('login/', view=views.user_login, name='login'),
    path('logout/', view=views.user_logout, name='logout'),

    # users - user posts -----------> (list - detail)
    path('users/', view=views.UserListView.as_view(), name='user_list'),
    path('user/<str:username>/', view=views.UserProfileView.as_view(), name='user_profile'),
    path('user/<str:username>/edit/', view=views.UserEditProfileView.as_view(), name='user_edit_profile'),
    path('user_posts/<str:username>/', view=views.UserPostListView.as_view(), name='user_post_list'),
    
    # followers - followings -----------> (list - add - delete)
    path('user_followers/<str:username>/', view=views.UserFollowerListView.as_view(), name='user_follower_list'),
    path('user_followings/<str:username>/', view=views.UserFollowingListView.as_view(), name='user_following_list'),
    
    path('follow/add/', view=views.AddFollowView.as_view(), name='add_follow'),
    path('follow/<str:to_user>/delete/<str:from_user>/', view=views.DeleteFollowView.as_view(), name='delete_follow'),

    
    # user favorites -----------> (list - add - delete)
    path('user_favorite-posts/<str:username>/', view=views.UserFavoritePostListView.as_view(), name='user_favorite_post_list'),
    path('favorite/add/', view=views.AddFavoriteView.as_view(), name='add_favorite'),
    path('favorite/<str:username>/delete/<int:post_id>/', view=views.DeleteFavoriteView.as_view(), name='delete_favorite'),
    
    # posts - post's like -----------> (list - detail - create - update - add - delete)
    path('posts/', view=views.PostListView.as_view(), name='post_list'),
    path('post/create/', view=views.PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', view=views.PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', view=views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/', view=views.PostDetailView.as_view(), name='post_list'),
    path('post/likes/<int:post_id>/', view=views.PostLikeListView.as_view(), name='post_likes'), # post like list
    path('post/like/add/', view=views.AddLikeView.as_view(), name='add_like'), # add
    path('post/<int:post_id>/like/delete/<str:username>/', view=views.DeleteLikeView.as_view(), name='delete_like'), # delete
]
