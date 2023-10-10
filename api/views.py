from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.models import User

from post.models import Post, Favorite
from .serializers import PostListSerializer, FollowerOrFollowingListSerializer, UserListSerializer



class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        srz_data = UserListSerializer(instance=users, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('id')
        srz_data_posts = PostListSerializer(instance=posts, many=True)

        for post in srz_data_posts.data:
            post['type'] = 'post'

        return Response(data=srz_data_posts.data, status=status.HTTP_200_OK)
 

class UserPostListView(APIView):
    def get(self, request, username):
        try:
            user = user = User.objects.get(username=username)
            posts = Post.objects.filter(user=user).order_by('id')
            srz_data_posts = PostListSerializer(instance=posts, many=True)
            return Response(data=srz_data_posts.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={f'{username}': 'this username does not exists.'}, status=status.HTTP_404_NOT_FOUND)
        

class UserFavoritePostListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            favorite_posts = Favorite.objects.get(user=user).post.all().order_by('id')
            srz_data_favorite_posts = PostListSerializer(instance=favorite_posts, many=True)
            return Response(data=srz_data_favorite_posts.data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response(data={f'{username}': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        
        except Favorite.DoesNotExist:
            return Response(data={f'{username}': "this username doesn't have favorite posts."}, status=status.HTTP_404_NOT_FOUND)
        

class UserFollowerListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = user.followers.all().order_by('id')
            srz_data = FollowerOrFollowingListSerializer(instance=followers, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={f'{username}': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)


class UserFollowingListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = user.followings.all().order_by('id')
            srz_data = FollowerOrFollowingListSerializer(instance=followers, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={f'{username}': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)

