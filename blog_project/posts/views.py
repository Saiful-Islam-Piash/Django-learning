from django.shortcuts import render,redirect
from . forms import PostForm
from .models import Posts

# Create your views here.
def add_posts(request):
    if request.method=='POST':
        post_form=PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_posts')
    else:
        post_form=PostForm()

    return render(request,'add_posts.html',{'form':post_form})

def edit_post(request,id):
    post=Posts.objects.get(pk=id)
    post_form=PostForm(instance=post)
    if request.method=='POST':
        post_form=PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    
    
    return render(request,'add_posts.html',{'form':post_form})


def delete_post(request,id):
    post=Posts.objects.get(pk=id)
    post.delete()
    return redirect('home')
    
    
    