from django.views.generic import DetailView

from Blog.models import Post


class PostDetailView(DetailView):
  model = Post
  template_name = 'Blog/post_detail.html'

  def get_context_data(self, *args, **kwargs):
    data = super().get_context_data(*args, **kwargs)

    post = self.get_object()
    post.content = post.content.split('\n')
    data['post'] = post

    return data
