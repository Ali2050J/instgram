from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from django.contrib.auth.models import User

from accounts.models import Relation
from post.models import Post, Favorite
from . import serializers


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        srz_data = serializers.UserListSerializer(instance=users, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('id')
        srz_data_posts = serializers.PostListSerializer(instance=posts, many=True)

        for post in srz_data_posts.data:
            post['type'] = 'post'

        return Response(data=srz_data_posts.data, status=status.HTTP_200_OK)
 

class UserPostListView(APIView):
    def get(self, request, username):
        try:
            user = user = User.objects.get(username=username)
            posts = Post.objects.filter(user=user).order_by('id')
            srz_data_posts = serializers.PostListSerializer(instance=posts, many=True)
            return Response(data=srz_data_posts.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detial': 'this username does not exists.'}, status=status.HTTP_404_NOT_FOUND)
        

class UserFavoritePostListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            favorite_posts = Favorite.objects.get(user=user).post.all().order_by('id')
            srz_data_favorite_posts = serializers.PostListSerializer(instance=favorite_posts, many=True)
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
            srz_data = serializers.UserListSerializer(instance=who_likes, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        
        except Post.DoesNotExist:
            return Response(data={'detail': "this post doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        

class UserFollowerListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = user.followers.all().order_by('id')
            srz_data = serializers.FollowerOrFollowingListSerializer(instance=followers, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)


class UserFollowingListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = user.followings.all().order_by('id')
            srz_data = serializers.FollowerOrFollowingListSerializer(instance=followers, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        

class AddFollowView(APIView):
    def post(self, request):
        srz_data = serializers.AddFollowersOrFollowingSerializer(data=request.POST)
        if srz_data.is_valid():
            try:
                from_user = User.objects.get(username=srz_data.data['from_user'])
                to_user = User.objects.get(username=srz_data.data['to_user'])
                try:
                    Relation.objects.get(from_user=from_user, to_user=to_user)
                except Relation.DoesNotExist:
                    Relation.objects.create(from_user=from_user, to_user=to_user)
                    
                return Response(srz_data.data, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
            
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteFollowView(APIView):
   def delete(self, request, from_user, to_user):
        from_user = User.objects.get(username=from_user)
        to_user = User.objects.get(username=to_user)
        try:
            Relation.objects.get(from_user=from_user, to_user=to_user).delete()
            return Response(data={'detail': f"{from_user} unfollowed {to_user}."}, status=status.HTTP_404_NOT_FOUND)
        
        except Relation.DoesNotExist:
            return Response(data={'detail': f"{from_user} don't following {to_user}."}, status=status.HTTP_404_NOT_FOUND)


class AddFavoriteView(APIView):
    def post(self, request):
        srz_data = serializers.AddFavoriteSerializer(data=request.data)
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
        srz_data = serializers.AddLikeSerializer(data=request.data)
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
    

class DeleteLikeView(APIView):
    def delete(self, request, username, post_id):
        try:
            user = User.objects.get(username=username)
            post = Post.objects.get(id=post_id)
            post.like.remove(user)
            return Response(data={'message': f"{user.username} unlike this post."}, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response(data={'detail': "this user doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        
        except Post.DoesNotExist:
            return Response(data={'detail': "this post doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
