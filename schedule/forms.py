from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title','description','day_of_week','time','notification_enabled']
        widgets = {
            'time': forms.TimeInput(format='%H:%M', attrs={'type':'time'}),
            'description': forms.Textarea(attrs={'rows':3}),
        }
