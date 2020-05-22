from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		#fields shown usr, email, password, pwd convifrmation
		fields = ['username', 'email', 'password1', 'password2']

class UserDataForm(forms.Form):
	### TODO: this needs some beautifying
	# TODO: make this a ModelForm so that we can save to DB
	your_name = forms.CharField()
	your_email = forms.EmailField()
	#offer_letter = forms.FileField()
	role = forms.CharField()
	company_name = forms.CharField()
	manager_name = forms.CharField()
	manager_email = forms.EmailField()
	recruiter_name = forms.CharField()
	recruiter_email = forms.EmailField()

	class Meta:
		#fields shown usr, email, password, pwd convifrmation
		fields = ['person_name',
		'person_email',
		'role',
		'company_name',
		'manager_name',
		'manager_email',
		'recruiter_name',
		'recruiter_email']
	