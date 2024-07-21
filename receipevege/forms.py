from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.forms import forms

class RegisterForm(UserChangeForm):
    class Meta:
        model = User

        fields = ['username','first_name','last_name','email','password']