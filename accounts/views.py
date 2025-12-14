from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from accounts.models import Profile 
from .forms import CustomSignupForm, ProfileUpdateForm


@login_required
def profile_view(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'form': form
    })


def signup(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST, request.FILES)  # include FILES for avatar
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            
            # Restrict to UTRGV emails
            if not email.endswith("@utrgv.edu"):
                form.add_error("email", "You must use a UTRGV email to sign up.")
            else:
                user = form.save(request)  # CustomSignupForm saves Profile too
                user.is_active = False  # disable until verified
                user.save()

                # Email verification
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                verify_url = f"{settings.SITE_DOMAIN}/accounts/verify/{uid}/{token}/"

                send_mail(
                    "Verify your Student Hub account",
                    f"Click the link to verify your account:\n\n{verify_url}",
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                )

                return render(request, "accounts/verify_sent.html")
    else:
        form = CustomSignupForm()

    return render(request, "accounts/signup.html", {"form": form})


def verify_email(request, uidb64, token):
    """
    Verify the user's email address using uidb64 and token.
    Activates the user if the token is valid.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("student-hub-home")

    # Verification failed
    return render(request, "accounts/verify_failed.html")
