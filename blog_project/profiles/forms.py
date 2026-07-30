from . models import Profile

from django import forms

class PofileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = "__all__"
