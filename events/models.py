from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('academic','Academic'),
    ('sports','Sports'),
    ('clubs','Clubs'),
]

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255, blank=True)
    map_link = models.URLField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"{self.title} ({self.category}) on {self.date}"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    class Meta:
        unique_together = ('user','category')
