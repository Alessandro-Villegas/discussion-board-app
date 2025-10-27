from django.contrib import admin
from .models import Post, Comment

# Admin viewing posts and comments
admin.site.register(Post)
admin.site.register(Comment)
