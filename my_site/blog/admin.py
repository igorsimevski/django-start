from django.contrib import admin
from .models import Post, Tag, Author

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("title",)
  list_display = ("title",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)