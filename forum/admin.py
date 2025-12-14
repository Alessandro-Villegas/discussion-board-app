from django.contrib import admin
from .models import Post, Comment

# # Admin viewing posts and comments
# admin.site.register(Post)
# admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_approved', 'created_at')
    list_editable = ('is_approved',)
    list_filter = ('is_approved',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'is_approved', 'created_at')
    list_editable = ('is_approved',)
    list_filter = ('is_approved',)
