from django.db import models
from django.contrib.auth.models import User

DAYS = [
    ('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),
    ('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday'),
]

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    day_of_week = models.CharField(max_length=10, choices=DAYS)
    time = models.TimeField()
    notification_enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['day_of_week', 'time']

    def __str__(self):
        return f"{self.title} ({self.day_of_week} @ {self.time})"
