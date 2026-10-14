from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'created_at']


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField( read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'username']



class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id','title', 'content','author', 'created_at', 'updated_at']

