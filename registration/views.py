from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from django.views.generic import CreateView,UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def logout_request(request):
    logout(request)
    messages.info(request,"Loggged out successfully!")
    return redirect('index')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now loggedin as {username}")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password")
                form = AuthenticationForm()
                return render(request,'registration/login.html',  {"form":form })
        else:
            messages.error(request,"invalid username or password")
            form = AuthenticationForm()
            return render(request,'registration/login.html',  {"form":form })
    else:
        form = AuthenticationForm()
        return render(request,'registration/login.html',  {"form":form })
    
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            login(request,user)
            return redirect('index')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request,'registration/register.html',{'form':form})
    form = NewUserForm()
    return render(request,'registration/register.html',{'form':form})


def homepage(request):
    return render(request,'registration/home.html')

