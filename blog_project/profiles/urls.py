from django.urls import path
from . import views

urlpatterns = [
    path('add_profiles/',views.add_profiles,name='add_profiles'),
]
