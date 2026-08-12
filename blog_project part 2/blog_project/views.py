from django.shortcuts import render
from posts.models import Posts
def home(request):
    data=Posts.objects.all()

    return render(request,'home.html',{'data':data})