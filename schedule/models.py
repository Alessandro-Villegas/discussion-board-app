from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField(default='09:00:00')  # Has a default
    end_time = models.TimeField(default='10:00:00')    # Has a default
    description = models.TextField(blank=True, default='')  # Allows blank
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.day_of_week}"

    class Meta:
        ordering = ['day_of_week', 'start_time']