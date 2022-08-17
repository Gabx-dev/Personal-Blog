import pytest

from django.contrib.auth.models import User
from Blog.models import Post


@pytest.mark.django_db
def test_post():
  user = User.objects.create_user('TestUser', 'user@test.io', '102030')
  post_title = 'Test post'
  post_slug = 'test-post'

  post = Post.objects.create(
    title=post_title,
    slug=post_slug,
    author=user
  )

  assert post.title == post_title
  assert post.slug == post_slug
  assert post.content == ''
  assert post.status == 0  # Draft

  assert Post.objects.filter().count() > 0