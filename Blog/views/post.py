from django.views.generic import DetailView

from Blog.models import Post
from Blog.models import Comment
from Blog.forms import CommentForm


class PostDetailView(DetailView):
  model = Post
  template_name = 'Blog/post_detail.html'

  def get_context_data(self, *args, **kwargs):
    data = super().get_context_data(*args, **kwargs)

    post = self.get_object()
    post.content = post.content.split('\n')

    comments = Comment.objects.filter(post=post)

    for i in range(len(comments)):
      comments[i].content = comments[i].content.split('\n')
    
    data['post'] = post
    data['comments'] = comments
    data['comment_count'] = comments.count()
    data['comment_form'] = CommentForm()

    return data

  def post(self, request, *args, **kwargs):
    comment = Comment(
      name=request.POST.get('name'),
      email=request.POST.get('email'),
      content=request.POST.get('content'),
      post=self.get_object()
    )
    comment.save()

    return self.get(self, request, *args, **kwargs)
