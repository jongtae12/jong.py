from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def user_profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})
