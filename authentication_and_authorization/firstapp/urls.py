from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup,name='signup'),
    path('login/', views.log_in,name='login'),
    path('logout/', views.log_out,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('pass_change/',views.pass_change,name='passchange')
]