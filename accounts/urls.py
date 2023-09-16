from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', view=views.UserRegisterView.as_view(), name='user_register'),
    path('login/', view=views.UserLoginView.as_view(), name='user_login'),
    path('logout/', view=views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/<int:pk>/', view=views.UserProfileView.as_view(), name='user_profile'),
    path('profile/edit/<int:pk>/', view=views.UserEditProfileView.as_view(), name='edit_profile'),
    path('follow/<int:user_id>/', view=views.UserFollowView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', view=views.UserUnfollowView.as_view(), name='unfollow_user'),
]
