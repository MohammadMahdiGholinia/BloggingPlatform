from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *
# Create your views here.

class PostView(APIView):
    def get (self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

class PostDetailView(APIView):
    def get(sef, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostDetailSerializer(post)

        return Response(serializer.data) 

