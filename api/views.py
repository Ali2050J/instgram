from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from accounts.models import Relation, Profile
from post.models import Post, Favorite
from story.models import Story
from . import serializers


# register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


# login
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(email=username).first() or authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

# logout
@api_view(['POST'])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# user list
class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        srz_data = serializers.UserListSerializer(instance=users, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


# user profile
class UserAllInfoProfileView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            srz_data = serializers.UserAllInfoProfileSerializer(instance=user)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detail': 'this username does not exists.'}, status=status.HTTP_404_NOT_FOUND)


# user detail
class UserProfileView(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=self.kwargs['username'])
            # profile = Profile.objects.get(user=user)
            srz_data = serializers.UserProfileSerializer(instance=user)
            return Response(srz_data.data)
        
        except User.DoesNotExist:
            return Response(data={'detial': 'this username does not exists.'}, status=status.HTTP_404_NOT_FOUND)
        
        except Profile.DoesNotExist:
            return Response(data={'detial': 'this username does not have profile.'}, status=status.HTTP_404_NOT_FOUND)


# user update
class UserEditProfileView(APIView):

    def put(self, request, username):
        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# user post list
class UserPostListView(APIView):
    def get(self, request, username):
        try:
            user = user = User.objects.get(username=username)
            posts = Post.objects.filter(user=user).order_by('id')
            srz_data_posts = serializers.PostListSerializer(instance=posts, many=True)
            return Response(data=srz_data_posts.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detial': 'this username does not exists.'}, status=status.HTTP_404_NOT_FOUND)
        

# user favorite post list
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

 
# all posts which user followers posted
class UserHomePostListView(generics.ListAPIView):
    serializer_class = serializers.PostListSerializer

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        user_followers = user.followers.all()
        posts = []
        for user in user_followers:
            for post in user.from_user.posts.all():
                posts.append(post)
        return posts


# # all stories which user followers posted
class UserHomeStoryListView(generics.ListAPIView):
    serializer_class = serializers.StorySerializer
    
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        user_followers = user.followers.all()
        stories = []
        for user in user_followers:
            for story in user.from_user.stories.all():
                stories.append(story)
        return stories   


# post list
class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('id')
        srz_data_posts = serializers.PostListSerializer(instance=posts, many=True)

        for post in srz_data_posts.data:
            post['type'] = 'post'

        return Response(data=srz_data_posts.data, status=status.HTTP_200_OK)
 

# post detail
class PostDetailView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs['post_id'])
        srz_post = serializers.PostDetailSerializer(instance=post)
        return Response(srz_post.data)
    

# post create
class PostCreateView(generics.CreateAPIView):
    serializer_class = serializers.PostCreateDeleteSerializer
    queryser = Post.objects.all()


# post update
class PostUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.PostUpdateSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        return super().perform_update(serializer)


# post delete
class PostDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.PostCreateDeleteSerializer
    queryset = Post.objects.all()


# post likes list(users)
class PostLikeListView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            who_likes = post.like.all().order_by('id')
            srz_data = serializers.UserListSerializer(instance=who_likes, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        
        except Post.DoesNotExist:
            return Response(data={'detail': "this post doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        

# user followers list(users)
class UserFollowerListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = user.followers.all().order_by('id')
            srz_data = serializers.FollowerOrFollowingListSerializer(instance=followers, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)


# # user followings list(users)
class UserFollowingListView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = user.followings.all().order_by('id')
            srz_data = serializers.FollowerOrFollowingListSerializer(instance=followers, many=True)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detail': "this username doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
        

# story detail and delete
class StoryDetailDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.StorySerializer
    queryset = Story.objects.all()


# add user to followers or following
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


# # delete user from followers or following
class DeleteFollowView(APIView):
   def delete(self, request, from_user, to_user):
        from_user = User.objects.get(username=from_user)
        to_user = User.objects.get(username=to_user)
        try:
            Relation.objects.get(from_user=from_user, to_user=to_user).delete()
            return Response(data={'detail': f"{from_user} unfollowed {to_user}."}, status=status.HTTP_404_NOT_FOUND)
        
        except Relation.DoesNotExist:
            return Response(data={'detail': f"{from_user} don't following {to_user}."}, status=status.HTTP_404_NOT_FOUND)


# add post to user favorite posts
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
    

# # delete post to user favorite posts
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
    

# add user to post likes (one user like a post)
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
    

# delete user from post likes (one user unlike a post)
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
