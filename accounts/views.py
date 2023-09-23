from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from borrowing_and_returning.models import Cart, BookItem

def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books')
    return render(request,'accounts/register.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        login(request, user)
        return redirect('books')
    return render(request, 'accounts/signin.html')


def user_logout(request):
    logout(request)
    return redirect('login')
