from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from .models import Profile

class CustomSignupForm(SignupForm):
    major = forms.CharField(max_length=100, label="Major")
    year = forms.CharField(max_length=20, label="Year")
    avatar = forms.ImageField(required=False)

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        # domain restrictions to UTRGV
        # if not email.endswith("@utrgv.edu"):
        #     raise ValidationError("You must use a UTRGV email address.")
        return email

    def save(self, request):
        user = super().save(request)
        Profile.objects.get_or_create(
            user=user,
            defaults={
                "major": self.cleaned_data["major"],
                "year": self.cleaned_data["year"],
                "avatar": self.cleaned_data.get("avatar"),
            }
        )
        return user
