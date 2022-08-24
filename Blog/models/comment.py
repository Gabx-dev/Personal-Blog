from django.db import models
from django.contrib.auth.models import User
from . import Post

class Comment(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=320)
  post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  content = models.TextField()
  active = models.BooleanField(default=False)

def __str__(self):
  return f'Comment by {self.creator} on {self.created_on}'