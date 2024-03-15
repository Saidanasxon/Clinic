from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django import forms


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,(f" Salom {user.first_name} {user.last_name} sizni yana ko'rib turganimizdan hursandmiz"))
                return redirect('index')
            else:
                messages.error(request,("Login yoki parolni notogri kiritdingiz  iltimos qayta urinib koring "))

    else:
        form = LoginForm()



    return render(request,'my_app/login.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,("Shaxsiy kabinetdan chiqdingiz"))
    return redirect('index')


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,(" Ro'yhatdan o'tish muvaffaqiyatli yakunlandi "))
            return HttpResponseRedirect(reverse('userauth:register')) 
            
    else:
        form = RegisterForm()
    return render(request, 'my_app/register.html', {'form': form})