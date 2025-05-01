from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    return render(request, "user_management/login.html")

def logout_view(request):
    logout(request)
    return render(request, "user_management/login.html")

@login_required(login_url='login')
def home(request):
    return render(request, "user_management/home.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        display_name = request.POST["display_name"]
        email = request.POST["email"]

        try:
            # Create User
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            # Create associated Profile
            profile = Profile.objects.create(user=user, display_name=display_name, email_address=email)
            profile.save()
        except:
            messages.error(request, "Username already taken.")
            return render(request, "user_management/register.html")
        
        login(request, user)
        return redirect("home")
    else:
        return render(request, "user_management/register.html")
    
def reset(request):
    return render(request, "user_management/password_reset_form.html")