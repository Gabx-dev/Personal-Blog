import pytest

from django.test import client
from django.contrib.auth.models import User
from django.urls import reverse

from Blog.models import Post

@pytest.mark.django_db()
def test_home(client):
  url = ''
  res = client.get(url)
  assert res.status_code == 200

@pytest.mark.django_db
def test_post(client):
  user = User.objects.create_user('testUser', 'user@test.io', '102030')
  post = Post.objects.create(
    title='Test post',
    slug='test-post',
    author=user,
    content='This is a test post'
  )

  url = reverse('post_detail', args=[post.slug])
  print(url)
  res = client.get(url)
  assert res.status_code == 200