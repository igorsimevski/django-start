from django.contrib import admin
from .models import Post, Tag, Author

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("title", "published_date", "tags")
  list_display = ("title", "published_date", "author")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)