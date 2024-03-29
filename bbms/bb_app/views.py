from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import new_user_login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse("worked!")

def users(request):
    form =new_user_login()
    if request.method=='POST':
        form=new_user_login(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    render(request,'bb_app/index.html',{'form':form})
    return HttpResponse("didnt work")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponse("logged out!")

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed!")
            return HttpResponse("invalid login details!")
    else:
        return render(request,'bb_app/index.html',{})
