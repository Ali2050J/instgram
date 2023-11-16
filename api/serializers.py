from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from post.models import Post
from accounts.models import Relation, Profile
from comment.models import Comment
from story.models import Story


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image', 'full_name', 'bio', 'gender')


class UserProfileSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile')

    def get_profile(self, obj):
        profile = obj.profile
        return ProfileSerializer(instance=profile).data
    

class UserAllInfoProfileSerializer(serializers.ModelSerializer):
    followers_quantity = serializers.SerializerMethodField()
    followings_quantity = serializers.SerializerMethodField()
    posts_quantity = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile', 'followers_quantity', 'followings_quantity', 'posts_quantity')

    def get_profile(self, obj):
        profile = obj.profile
        return ProfileSerializer(instance=profile).data
    
    def get_followers_quantity(self, obj):
        followers_quantity = obj.followers.count()
        return followers_quantity
    
    def get_followings_quantity(self, obj):
        followings_quantity = obj.followings.count()
        return followings_quantity
    
    def get_posts_quantity(self, obj):
        posts_quantity = obj.posts.count()
        return posts_quantity



class PostListSerializer(serializers.ModelSerializer):
    likes_quantity = serializers.SerializerMethodField()
    comments_quantity = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = '__all__'

    def get_likes_quantity(self, obj):
        likes = obj.like.all().count()
        return likes
    
    def get_comments_quantity(self, obj):
        comments = obj.comments.all().count()
        return comments
    
    def get_user(self, obj):
        return UserProfileSerializer(instance=obj.user).data


class StorySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = '__all__'

    def get_user(self, obj):
        return UserProfileSerializer(instance=obj.user).data


class CommentListSerializer(serializers.ModelSerializer):
    reply_comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = '__all__'

    def get_reply_comments(self, obj):
        reply_comments = obj.replies.all()
        return CommentListSerializer(instance=reply_comments, many=True).data


class PostDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentListSerializer(instance=comments, many=True).data


class PostCreateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'caption', 'status')


class FollowerOrFollowingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'


class AddFavoriteSerializer(serializers.Serializer):
    user = serializers.CharField()
    post = serializers.CharField()


class AddLikeSerializer(serializers.Serializer):
    post = serializers.CharField()
    user = serializers.CharField()


class AddFollowersOrFollowingSerializer(serializers.Serializer):
    from_user = serializers.CharField()
    to_user = serializers.CharField()
