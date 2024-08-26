from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def service_view(request):
    return render(request, 'service.html')


def contact_view(request):
    return render(request, 'contact.html')


def blog_view(request):
    return render(request, 'blog.html')


def portfolio_view(request):
    return render(request, 'portfolio.html')


def about_view(request):
    return render(request, 'about.html')


def logout_view(request):
    logout(request)
    return redirect('authentication')


def profile_view(request):
    return render(request, 'profile.html')