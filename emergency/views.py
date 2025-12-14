from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EmergencyContact
from .forms import EmergencyContactForm


def emergency_list(request):
    high_priority = EmergencyContact.objects.filter(priority='high').order_by('name')
    medium_priority = EmergencyContact.objects.filter(priority='medium').order_by('name')
    low_priority = EmergencyContact.objects.filter(priority='low').order_by('name')
    
    return render(request, 'emergency/emergency_list.html', {
        'high_priority_contacts': high_priority,
        'medium_priority_contacts': medium_priority,
        'low_priority_contacts': low_priority,
    })


@login_required
def add_emergency(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emergency-list')
    else:
        form = EmergencyContactForm()
    
    return render(request, 'emergency/emergency_form.html', {
        'form': form,
        'title': 'Add Emergency Contact'
    })


@login_required
def edit_emergency(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk)
    
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('emergency-list')
    else:
        form = EmergencyContactForm(instance=contact)
    
    return render(request, 'emergency/emergency_form.html', {
        'form': form,
        'title': 'Edit Emergency Contact'
    })


@login_required
def delete_emergency(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('emergency-list')
    
    return render(request, 'emergency/emergency_confirm_delete.html', {
        'contact': contact
    })