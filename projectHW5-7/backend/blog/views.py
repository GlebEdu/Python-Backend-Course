from django.shortcuts import render
from rest_framework import generics
from .models import Post, Comment, PostLike, CommentLike
from .serializers import PostSerializer, CommentSerializer, PostLikeSerializer, CommentLikeSerializer

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
