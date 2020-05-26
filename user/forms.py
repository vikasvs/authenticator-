from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserData

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		#fields shown usr, email, password, pwd convifrmation
		fields = ['username', 'email', 'password1', 'password2']

class UserDataForm(forms.ModelForm):
	class Meta:
		#fields shown usr, email, password, pwd convifrmation
		model = UserData
		fields = ['your_name',
		'your_email',
		#'offer_letter',
		'role',
		'company_name',
		'manager_name',
		'manager_email',
		'recruiter_name',
		'recruiter_email']
	