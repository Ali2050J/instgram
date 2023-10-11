from django.contrib.auth.models import User
from rest_framework import serializers
from post.models import Post, Favorite
from accounts.models import Relation


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


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
