from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = [
    'title',
    'author',
    'created_on',
    'published_on',
    'status'
  ]

  list_filter = ['status', 'created_on']
  prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  pass