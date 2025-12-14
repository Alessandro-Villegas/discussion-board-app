from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from .models import Profile


class CustomSignupForm(SignupForm):
    """Custom signup form that includes avatar during registration"""
    avatar = forms.ImageField(required=False)
    major = forms.CharField(max_length=100, required=False)
    year = forms.CharField(max_length=20, required=False)

    def save(self, request):
        user = super().save(request)
        # Profile is auto-created by signal, so just update it
        profile = user.profile
        profile.avatar = self.cleaned_data.get('avatar')
        profile.major = self.cleaned_data.get('major', '')
        profile.year = self.cleaned_data.get('year', '')
        profile.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    """Form for updating user profile - this one doesn't need request"""
    class Meta:
        model = Profile
        fields = ['avatar', 'major', 'year']
        widgets = {
            'major': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Computer Science'
            }),
            'year': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('', 'Select Year'),
                ('Freshman', 'Freshman'),
                ('Sophomore', 'Sophomore'),
                ('Junior', 'Junior'),
                ('Senior', 'Senior'),
                ('Graduate', 'Graduate'),
            ]),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
