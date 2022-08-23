from django.http import HttpResponse
from django.template import loader

from Blog.models import Post


def postDetailView(request, slug):
  post = Post.objects.get(slug=slug)
  post.content = post.content.split('\n')
  template = loader.get_template('Blog/post_detail.html')

  context ={
    'post': post
  }
  
  return HttpResponse(template.render(context, request))