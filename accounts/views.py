from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import CustomUserCreationForm
from accounts.models import UserProfile


def user_profile(request):
    return render(request, 'registration/user_profile.html')


def signup_user(request):
    if request.method == "GET":
        context = {
            'form': CustomUserCreationForm(),
        }
        return render(request, 'registration/registration.html', context)
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user
            )
            profile.save()
            return redirect('common index')


def sign_out_user(request):
    logout(request)
    return redirect('common index')
