from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a 'home' page after successful login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'myapp/login.html')



def forgot_user_id_view(request):
    return render(request, 'myapp/forgot_user_id.html')


def verify_code(request):
    return render(request, 'myapp/verify_code.html')

def forgot_password_view(request):
    return render(request, 'myapp/forgot_password.html')

def verify_password(request):
    return render(request, 'myapp/verify_password.html')

def set_password(request):
    return render(request, 'myapp/set_password.html')