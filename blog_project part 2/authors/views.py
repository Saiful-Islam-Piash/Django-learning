from django.shortcuts import render,redirect
from .forms import RegistrationForm ,ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
# def add_author(request):
#     if request.method == "POST":
#         author_form=AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')

#     else:
#         author_form=AuthorForm()

#     return render(request,'add_author.html',{'form':author_form})


def register(request):
    if request.method == "POST":
        register_form=RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('register')
    else:
        register_form=RegistrationForm()
    return render(request,'register.html',{'form':register_form,'type':'Register'})

def user_login(request):
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user= authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request,'Logged in Successfully')
                login(request,user)
                return redirect('user_login')
            else:
                messages.warning(request,'Login information is incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request,'register.html',{'form':form,'type':'Login'})
@login_required
def profile(request):
    if request.method == "POST":
        profile_form=ChangeUserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('register')
    else:
        profile_form=ChangeUserForm()
    return render(request,'profile.html',{'form':profile_form})
