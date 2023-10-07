from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from post.models import Post
from .serializers import PostListSerializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('id')
        srz_date = PostListSerializer(instance=posts, many=True)
        return Response(data=srz_date.data, status=status.HTTP_200_OK)
