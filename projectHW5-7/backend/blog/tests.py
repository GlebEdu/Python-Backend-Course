from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Post, Comment, PostLike, CommentLike
from .serializers import CommentSerializer, PostSerializer

class APITestCaseWithAuth(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.filter(username="testuser").delete()
        cls.user = User.objects.create_user(username="testuser", password="testpassword")
        cls.token = RefreshToken.for_user(cls.user)
        cls.auth_header = {'HTTP_AUTHORIZATION': f'Bearer {cls.token.access_token}'}
        cls.post = Post.objects.create(title="Test Post", content="This is a test post", author=cls.user)

    def test_create_post(self):
        url = '/api/posts/'
        data = {"title": "New Post", "content": "Post content", "author": self.user.id}
        response = self.client.post(url, data, **self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Post")
        self.assertEqual(response.data['content'], "Post content")

    def test_get_posts(self):
        url = '/api/posts/'
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Post")

    def test_update_post(self):
        url = f'/api/posts/{self.post.id}/'
        data = {"title": "Updated Post", "content": "Updated content", "author": self.user.id}
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = client.put(url, data, format='json')      
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Post")
        self.assertEqual(response.data['content'], "Updated content")
    
    def test_get_post(self):
        url = f'/api/posts/{self.post.id}/'
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Post")
        self.assertEqual(response.data['content'], "This is a test post")

    def test_delete_post(self):
        post_to_delete = Post.objects.create(
            title="Post to Delete", 
            content="This post will be deleted", 
            author=self.user
        )
        url = f'/api/posts/{post_to_delete.id}/'
        response = self.client.delete(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=post_to_delete.id).exists())

    def test_create_comment(self):
        url = '/api/comments/'
        data = {"content": "This is a comment", "author": self.user.id, "post": self.post.id}
        response = self.client.post(url, data, **self.auth_header, format='json')
        self .assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], "This is a comment")
        self.assertEqual(response.data['post'], self.post.id)

    def test_get_comments(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        url = f'/api/comments/'       
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], "Test comment")
    
    def test_get_comment(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        url = f'/api/comments/{comment.id}/'
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], "Test comment")
        self.assertEqual(response.data['post'], self.post.id)

    def test_update_comment(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        url = f'/api/comments/{comment.id}/'
        data = {"content": "Updated comment", "author": self.user.id, "post": self.post.id}
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], "Updated comment")

    def test_delete_comment(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        url = f'/api/comments/{comment.id}/'
        response = self.client.delete(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())

    def test_like_post(self):
        url = f'/api/postlikes/'
        data = {"user": self.user.id, "post": self.post.id}
        response = self.client.post(url, data, **self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_like_comment(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        url = f'/api/commentlikes/'
        data = {"user": self.user.id, "comment": comment.id}
        response = self.client.post(url, data, **self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unlike_post(self):
        like = PostLike.objects.create(user=self.user, post=self.post)
        url = f'/api/postlikes/{like.id}/' 
        response = self.client.delete(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unlike_comment(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        like = CommentLike.objects.create(user=self.user, comment=comment)
        url = f'/api/commentlikes/{like.id}/' 
        response = self.client.delete(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_post_likes(self):
        PostLike.objects.create(user=self.user, post=self.post)
        url = '/api/postlikes/'
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['post'], self.post.id)

    def test_get_post_like(self):
        like = PostLike.objects.create(user=self.user, post=self.post)
        url = f'/api/postlikes/{like.id}/'
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['post'], self .post.id)

    def test_update_post_like(self):
        like = PostLike.objects.create(user=self.user, post=self.post)
        url = f'/api/postlikes/{like.id}/'
        data = {"user": self.user.id, "post": self.post.id}
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = client.put(url, data, format='json')       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['post'], self.post.id)

    def test_get_comment_likes(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        CommentLike.objects.create(user=self.user, comment=comment)
        url = '/api/commentlikes/'
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['comment'], comment.id)

    def test_get_comment_like(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        like = CommentLike.objects.create(user=self.user, comment=comment)
        url = f'/api/commentlikes/{like.id}/'
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comment'], comment.id)

    def test_update_comment_like(self):
        comment = Comment.objects.create(content="Test comment", author=self.user, post=self.post)
        like = CommentLike.objects.create(user=self.user, comment=comment)
        url = f'/api/commentlikes/{like.id}/'
        data = {"user": self.user.id, "comment": comment.id}
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = client.put(url, data, format='json')     
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comment'], comment.id)

    def test_get_posts_with_likes(self):
        PostLike.objects.create(user=self.user, post=self.post)
        url = '/api/posts/with-likes/'
        response = self.client.get(url, **self.auth_header)     
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.post.title)
        self.assertEqual(response.data[0]['likes_count'], 1)