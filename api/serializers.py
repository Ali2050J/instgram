from rest_framework import serializers
from post.models import Post, Favorite


class PostListSerializer(serializers.ModelSerializer):
    type = 'post'
    class Meta:
        model = Post
        fields = '__all__'


class FavoritePostListSerializer(serializers.ModelSerializer):
    type = 'favorite'

    class Meta:
        model = Favorite
        fields = '__all__'
