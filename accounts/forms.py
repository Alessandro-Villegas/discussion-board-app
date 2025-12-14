from django import forms
from .models import Profile
from allauth.account.forms import BaseSignupForm

class CustomSignupForm(BaseSignupForm):
    major = forms.CharField(max_length=100, required=True, label="Major")
    year = forms.CharField(max_length=20, required=True, label="Year")
    avatar = forms.ImageField(required=False, label="Avatar")

    def save(self, request):
        user = super().save(request)
        Profile.objects.create(
            user=user,
            major=self.cleaned_data['major'],
            year=self.cleaned_data['year'],
            avatar=self.cleaned_data.get('avatar')
        )
        return user
