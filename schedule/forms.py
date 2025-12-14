from django import forms
from .models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'day_of_week', 'start_time', 'end_time', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Software Engineering Lecture'
            }),
            'day_of_week': forms.Select(attrs={
                'class': 'form-select'
            }),
            'start_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',  # This is important for time input
            }),
            'end_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',  # This is important for time input
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional details about this activity',
                'rows': 3
            })
        }