from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
    
                for field in self.fields.values():
                    field.help_text = None

    class Meta:
        model= User
        fields=['username','first_name','last_name','email']

        