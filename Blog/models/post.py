from django.db import models
from django.contrib.auth.models import User

STATUS = (
  (0, 'draft'),
  (1, 'published')
)

class Post(models.Model):
  class Meta:
    ordering = ['-created_on']

    def __str__(self):
      return self.title
    
  title = models.CharField(max_length=255, unique=True)
  slug = models.SlugField(max_length= 255, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  created_on = models.DateTimeField(auto_now_add=True)
  published_on = models.DateTimeField(null=True)
  updated_on = models.DateTimeField(null=True)

  content = models.TextField()

  status = models.IntegerField(choices=STATUS, default=0)

  def __str__(self):
    return self.title