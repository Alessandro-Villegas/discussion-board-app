from django.shortcuts import render
from .models import EmergencyContact

def contact_list(request):
    contacts = EmergencyContact.objects.all()
    return render(request, 'emergency/emergency.html', {'contacts': contacts})
