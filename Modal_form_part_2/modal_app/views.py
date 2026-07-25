from django.shortcuts import render
from modal_app.forms import StudentForm

# Create your views here.
def home(request):
    if request.method=='POST':
        std=StudentForm(request.POST)
        if std.is_valid():
            std.save(commit=True)
            print(std.cleaned_data)
    else:
        std=StudentForm()

    return render(request,'home.html',{'std':std})
