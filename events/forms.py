from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','description','date','time','category','location','map_link']
        widgets = {'date': forms.DateInput(attrs={'type':'date'}), 'time': forms.TimeInput(attrs={'type':'time'})}
