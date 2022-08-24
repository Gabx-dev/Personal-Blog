import pytest

from django.contrib.auth.models import User

from Blog.models import Post
from Blog.models import Comment


user_data = ['TestUser', 'user@test.io', '102030']
post_data = {'title': 'Test post', 'slug': 'test-post'}
comment_data = {
  'name': 'Test User',
  'email': 'user@test.io',
  'content': 'Test comment'
}

@pytest.mark.django_db
def test_post():
  user = User.objects.create_user(*user_data)

  post = Post.objects.create(**post_data, author=user)

  assert post.title == post_data['title']
  assert post.slug == post_data['slug']
  assert post.content == ''
  assert post.status == 0  # Draft

  assert Post.objects.filter().count() > 0

@pytest.mark.django_db
def test_comment():
  user = User.objects.create_user(*user_data)
  post = Post.objects.create(**post_data, author=user)
  comment = Comment.objects.create(**comment_data, post=post)

  assert comment.name == comment_data['name']
  assert comment.email == comment_data['email']
  assert comment.content == comment_data['content']
  assert comment.post == post
  assert comment.active == False

  assert post.comment.all().count() > 0

  assert Comment.objects.all().count() > 0
