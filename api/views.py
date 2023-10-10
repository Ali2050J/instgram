from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.models import User

from post.models import Post, Favorite
from .serializers import PostListSerializer, FollowerOrFollowingListSerializer, UserListSerializer, AddFavoriteSerializer, AddLikeSerializer



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
            return Response(data={'detial': 'this username does not exists.'}, status=status.HTTP_404_NOT_FOUND)
        

class UserFavoritePostListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            favorite_posts = Favorite.objects.get(user=user).post.all().order_by('id')
            srz_data_favorite_posts = PostListSerializer(instance=favorite_posts, many=True)
            return Response(data=srz_data_favorite_posts.data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        
        except Favorite.DoesNotExist:
            return Response(data={'detail': "this username doesn't have favorite posts."}, status=status.HTTP_404_NOT_FOUND)
        

class PostLikeListView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            who_likes = post.like.all().order_by('id')
            srz_data = UserListSerializer(instance=who_likes, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        
        except Post.DoesNotExist:
            return Response(data={'detail': "this post doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        

class UserFollowerListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = user.followers.all().order_by('id')
            srz_data = FollowerOrFollowingListSerializer(instance=followers, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)


class UserFollowingListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = user.followings.all().order_by('id')
            srz_data = FollowerOrFollowingListSerializer(instance=followers, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)


class AddFavoriteView(APIView):
    def post(self, request):
        srz_data = AddFavoriteSerializer(data=request.data)
        if srz_data.is_valid():
            try:
                user = User.objects.get(username=srz_data.data['user'])
                post = Post.objects.get(id=srz_data.data['post'])
                user_favorite = Favorite.objects.get(user=user)
                user_favorite.post.add(post)
                return Response(srz_data.data, status=status.HTTP_201_CREATED)
            
            except User.DoesNotExist:
                return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
            
            except Post.DoesNotExist:
                return Response(data={'detail': "this post doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
            
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteFavoriteView(APIView):
    def delete(self, request, username, post_id):
        try:
            user = User.objects.get(username=username)
            user_favorites = Favorite.objects.get(user=user)
            post = Post.objects.get(id=post_id)
            user_favorites.post.remove(post)
            return Response(data={'message': f"this post remove from {username}'s post favorites"}, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response(data={'detail': "this user doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        
        except Post.DoesNotExist:
            return Response(data={'detail': "this post doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
    

class AddLikeView(APIView):
    def post(self, request):
        srz_data = AddLikeSerializer(data=request.data)
        if srz_data.is_valid():
            try:
                user = User.objects.get(username=srz_data.data['user'])
                post = Post.objects.get(id=srz_data.data['post'])
                post.like.add(user)
                return Response(srz_data.data, status=status.HTTP_201_CREATED)
            
            except User.DoesNotExist:
                return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
            
            except Post.DoesNotExist:
                return Response(data={'detail': "this post doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
            
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
