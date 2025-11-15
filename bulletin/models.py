from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title

