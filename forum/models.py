from django.db import models
from django.utils import timezone

# Post class
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    author = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
    
# Comment class
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    author = models.CharField(max_length = 100)
    text = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
