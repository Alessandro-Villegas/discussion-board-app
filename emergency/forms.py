from django import forms
from .models import EmergencyContact


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['name', 'phone_number', 'description', 'department', 'website', 'priority']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., UTRGV Police Department'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., (956) 665-2737'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Brief description of this contact',
                'rows': 3
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Police Directory'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com (optional)'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            })
        }