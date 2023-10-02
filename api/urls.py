from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('posts/', view=views.PostListView.as_view(), name='post_list'),
]
