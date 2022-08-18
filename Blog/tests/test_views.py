import pytest

from django.test import client

def test_home(client):
  url = ''
  response_content = b'Hello World!'

  res = client.get(url)

  assert res.status_code == 200
  assert res.content == response_content