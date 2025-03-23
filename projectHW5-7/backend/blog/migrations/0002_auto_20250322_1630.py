from django.db import migrations

def create_mock_data(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Post = apps.get_model("blog", "Post")
    Comment = apps.get_model("blog", "Comment")
    PostLike = apps.get_model("blog", "PostLike")
    CommentLike = apps.get_model("blog", "CommentLike")

    user = User.objects.create_user(username="testuser", password="testpass")

    post1 = Post.objects.create(title="Первый пост", content="Содержимое первого поста", author=user)
    post2 = Post.objects.create(title="Второй пост", content="Содержимое второго поста", author=user)

    comment1 = Comment.objects.create(content="Первый комментарий", post=post1, author=user)
    comment2 = Comment.objects.create(content="Второй комментарий", post=post2, author=user)

    PostLike.objects.create(user=user, post=post1)
    PostLike.objects.create(user=user, post=post2)
    CommentLike.objects.create(user=user, comment=comment1)
    CommentLike.objects.create(user=user, comment=comment2)

def remove_mock_data(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Post = apps.get_model("blog", "Post")
    Comment = apps.get_model("blog", "Comment")
    PostLike = apps.get_model("blog", "PostLike")
    CommentLike = apps.get_model("blog", "CommentLike")

    CommentLike.objects.all().delete()
    PostLike.objects.all().delete()
    Comment.objects.all().delete()
    Post.objects.all().delete()
    User.objects.filter(username="testuser").delete()

class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_mock_data, remove_mock_data),
    ]
