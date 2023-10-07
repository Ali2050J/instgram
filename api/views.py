from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from post.models import Post, Favorite
from .serializers import PostListSerializer, FavoritePostListSerializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('id')
        favorite_posts = Favorite.objects.all().order_by('id')
        # serializers
        srz_data_posts = PostListSerializer(instance=posts, many=True)
        srz_data_favorites = FavoritePostListSerializer(instance=favorite_posts, many=True)
        for favorite_p in srz_data_favorites.data:
            favorite_p['type'] = 'favorite'

        for post in srz_data_posts.data:
            post['type'] = 'post'
        all = srz_data_posts.data + srz_data_favorites.data # Merge two data
        return Response(data=all, status=status.HTTP_200_OK)
