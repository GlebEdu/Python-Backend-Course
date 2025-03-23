from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView, CommentRetrieveUpdateDestroyView, PostLikeListCreateView, PostLikeRetrieveUpdateDestroyView, CommentLikeListCreateView, CommentLikeRetrieveUpdateDestroyView, PostWithLikesCountView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),

    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),

    path('postlikes/', PostLikeListCreateView.as_view(), name='postlike-list-create'),
    path('postlikes/<int:pk>/', PostLikeRetrieveUpdateDestroyView.as_view(), name='postlike-retrieve-update-destroy'),

    path('commentlikes/', CommentLikeListCreateView.as_view(), name='commentlike-list-create'),
    path('commentlikes/<int:pk>/', CommentLikeRetrieveUpdateDestroyView.as_view(), name='commentlike-retrieve-update-destroy'),

    path('posts/with-likes/', PostWithLikesCountView.as_view(), name='post-with-likes-count'),

]
