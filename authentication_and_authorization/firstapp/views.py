from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
# Create your views here.
def signup(request):
    if not request.user.is_authenticated:

        if request.method =='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account created succesfully')
                # messages.info(request,'account info')
                # messages.warning(request,'account warning ')
                form.save()
                return redirect('signup')
        else:
            form=RegisterForm()
    else:
        return redirect('profile')
        
    return render(request,'signup.html',{'form':form})

def home(request):
    return render(request,'home.html')

def log_in(request):
    if not request.user.is_authenticated:

        if request.method =='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user=authenticate(username=name,password=userpass)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form=AuthenticationForm()
    else:
        return redirect('profile')

    return render(request,'login.html',{'form':form})


def profile(request):
    return render(request,'profile.html',{'user':request.user})

def log_out(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(form.cleaned_data['user']) #password update korbe
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'passchange.html',{'form':form})

