from django.contrib import admin
from . models import Post

@admin.register
class PostAdmin(Post):
    list_display = ('title','body','status','author')


admin.site.register(Post)