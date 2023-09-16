from django.urls import path

from . import views

app_name = 'comment'

urlpatterns = [
    path('create/<int:post_id>/', view=views.CreateCommentView.as_view(), name='create_comment'),
]
