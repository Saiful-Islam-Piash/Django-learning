from django.urls import path
from . import views

urlpatterns = [
    path('add_posts/',views.add_posts,name='add_posts'),
]
