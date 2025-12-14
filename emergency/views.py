from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import EmergencyContact
from .forms import EmergencyContactForm


def emergency_list(request):
    """Public view - anyone can see emergency contacts"""
    high_priority = EmergencyContact.objects.filter(priority='high').order_by('name')
    medium_priority = EmergencyContact.objects.filter(priority='medium').order_by('name')
    low_priority = EmergencyContact.objects.filter(priority='low').order_by('name')
    
    return render(request, 'emergency/emergency_list.html', {
        'high_priority_contacts': high_priority,
        'medium_priority_contacts': medium_priority,
        'low_priority_contacts': low_priority,
    })


@staff_member_required  # Only admin/staff can access
def add_emergency(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emergency contact added successfully!')
            return redirect('emergency-list')
    else:
        form = EmergencyContactForm()
    
    return render(request, 'emergency/emergency_form.html', {
        'form': form,
        'title': 'Add Emergency Contact'
    })


@staff_member_required  # Only admin/staff can access
def edit_emergency(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk)
    
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emergency contact updated successfully!')
            return redirect('emergency-list')
    else:
        form = EmergencyContactForm(instance=contact)
    
    return render(request, 'emergency/emergency_form.html', {
        'form': form,
        'title': 'Edit Emergency Contact'
    })


@staff_member_required  # Only admin/staff can access
def delete_emergency(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk)
    
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Emergency contact deleted successfully!')
        return redirect('emergency-list')
    
    return render(request, 'emergency/emergency_confirm_delete.html', {
        'contact': contact
    })