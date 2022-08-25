from django import forms

from Blog.models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['name', 'email', 'content']
  
  name = forms.CharField(label='Nome')
  email = forms.EmailField(label='E-mail')
  content = forms.CharField(label='Comentário', widget=forms.Textarea)