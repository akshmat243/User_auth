from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProfileForm
from .models import SlideCarousel, TeamMember, WebServices
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from datetime import timedelta

# Create your views here.
def index_view(request):
    carosels = SlideCarousel.objects.all()
    teams = TeamMember.objects.all()
    webservices = WebServices.objects.all()
    return render(request, 'accounts/index.html', {'carosels': carosels, 'teams': teams, 'webservices':webservices})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
                        
            if user is not None:
                remember_me = request.POST.get('remember_me')
                if remember_me == 'on':
                    request.session.set_expiry(30)  # 2 weeks   --    (timedelta(days = 14))
                else:
                    request.session.set_expiry(0)  # Expires when browser closes
                messages.success(request, 'Successfully logged in')
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username /or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    messages.success(request, 'Successfully logged out')
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/signup.html', {'form': form})


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/test.html')

@login_required(login_url='login')
def create_profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile created successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = ProfileForm(instance=request.user)
        return render(request, 'accounts/create_profile.html', {'form': form})








from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'passwords/password_reset.html'
    email_template_name = 'passwords/password_reset_email.html'
    subject_template_name = 'passwords/password_reset_subject.txt'

    success_url = reverse_lazy('password_reset_done')
    
