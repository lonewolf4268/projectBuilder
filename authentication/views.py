from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split('@')[0] + (email.split('@')[1]).split('.')[0]

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            login(request, user)
            return redirect('dashboard')
        except Exception as e:
            error_message = str(e)
            return render(request, 'register.html', {'error': error_message})
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            username = user.username
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = "Invalid email or password"
                return render(request, 'login.html', {'error': error_message})
        except User.DoesNotExist:
            error_message = "Email not found"
            return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html')