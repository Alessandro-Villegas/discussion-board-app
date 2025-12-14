from django.db import models


class EmergencyContact(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High Priority'),
        ('medium', 'Medium Priority'),
        ('low', 'Low Priority'),
    ]
    
    name = models.CharField(max_length=200, default='Unnamed Contact')
    phone_number = models.CharField(max_length=20, default='000-000-0000')
    description = models.TextField(blank=True, default='')
    department = models.CharField(max_length=200, blank=True, default='')
    website = models.URLField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-priority', 'name']