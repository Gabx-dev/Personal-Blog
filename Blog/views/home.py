from django.views.generic import TemplateView

from Blog.models import Post


class HomePageView(TemplateView):
  template_name = 'Blog/index.html'
  model = Post

  def get_context_data(self):
    data = super().get_context_data()
    posts = Post.objects.filter().order_by('created_on')
    data['post_list'] = posts
    return data
