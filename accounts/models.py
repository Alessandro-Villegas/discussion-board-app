from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.png", blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Signal to auto-create Profile
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    Profile.objects.get_or_create(user=instance)
