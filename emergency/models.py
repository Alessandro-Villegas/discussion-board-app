from django.db import models

class EmergencyContact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    department = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)

    def __str__(self): return f"{self.name} ({self.phone})"
