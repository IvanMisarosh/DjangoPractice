from django.contrib import admin
from .models import Author, Post, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", 'date')
    list_display = ("title", "date", "author",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "text", "post")

# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)



# ivan
# admin