from django.contrib import admin
from .models import Author, Post, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", 'date')
    list_display = ("title", "date", "author",)

# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)



# ivan
# admin