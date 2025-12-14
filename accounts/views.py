from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # disable until verified
            user.save()

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
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("student-hub-home")

    return render(request, "accounts/verify_failed.html")

