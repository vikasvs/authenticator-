from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#form that specifies what information we're collecting upon registration

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']