from django.http import HttpResponse
from django.template import loader

from Blog.models import Post


def homePageView(request):
  posts = Post.objects.filter().order_by('created_on')
  template = loader.get_template('Blog/index.html')

  context = {
    'post_list': posts
  }

  return HttpResponse(template.render(context, request))