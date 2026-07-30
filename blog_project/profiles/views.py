from django.shortcuts import render,redirect
from .forms import PofileForm

# Create your views here.
def add_profiles(request):
    if request.method=='POST':
        profile_form=PofileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profiles')

    else:
        profile_form=PofileForm()

    return render(request,'add_profiles.html',{'profile_form':profile_form})
