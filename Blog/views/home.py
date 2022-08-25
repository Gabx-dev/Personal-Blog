from django.views.generic import TemplateView

from Blog.models import Post


class HomePageView(TemplateView):
  model = Post
  template_name = 'Blog/index.html'

  def get_context_data(self):
    data = super().get_context_data()
    
    post_list = Post.objects.filter().order_by('created_on')
    data['post_list'] = post_list

    return data
