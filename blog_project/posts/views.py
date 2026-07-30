from django.shortcuts import render

# Create your views here.
def add_posts(request):
    return render(request,'add_posts.html')