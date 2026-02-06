from django.contrib import admin
from .models import Post, Tag, Author, Comment

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("title", "published_date", "tags")
  list_display = ("title", "published_date", "author")

class CommentAdmin(admin.ModelAdmin):
  list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)