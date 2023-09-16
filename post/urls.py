from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('create/', view=views.PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>/', view=views.PostEditView.as_view(), name='post_edit'),
    path('like/<int:post_id>/', view=views.PostLikeView.as_view(), name='post_like'),
    path('save/<int:pk>/', view=views.SavePostView.as_view(), name='post_save'),
    path('unsave/<int:pk>/', view=views.UnSavePostView.as_view(), name='post_unsave'),
]
