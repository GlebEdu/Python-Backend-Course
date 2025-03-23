from django.shortcuts import render
from rest_framework import generics
from .models import Post, Comment, PostLike, CommentLike
from .serializers import PostSerializer, CommentSerializer, PostLikeSerializer, CommentLikeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostLikeListCreateView(generics.ListCreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

class PostLikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

class CommentLikeListCreateView(generics.ListCreateAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer

class CommentLikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer

class PostWithLikesCountView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        posts_with_likes = []
        
        for post in posts:
            likes_count = PostLike.objects.filter(post=post).count()
            post_data = PostSerializer(post).data
            post_data['likes_count'] = likes_count
            posts_with_likes.append(post_data)

        return Response(posts_with_likes)

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
