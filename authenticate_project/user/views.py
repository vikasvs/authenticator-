from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserDataForm
from .main import verify_and_send
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			#username = form.cleaned_data.get('username')
			messages.success(request, f'You can now login!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form})

def employee(request):
	# need to create a custom form
	if request.method == 'POST':
		form = UserDataForm(request.POST)
		if form.is_valid():
			# TODO: POC logic goes here
			verify_and_send(form)
			form.save()
			messages.success(request, f'success')
			return redirect('profile') ###
	else:
		form = UserDataForm()
	return render(request, 'user/employee.html', {'form': form})

def reroute(request):
	return render(request, 'user/reroute.html')
#decorator that adds functionality saying you have to be logged in to see your profile -PROBABLY WONT NEED 

@login_required
def profile(request):
	if request.method == 'POST':
		form = UserDataForm(request.POST, request.FILES)
		if form.is_valid():
			# TODO: POC logic goes here
			verify_and_send(form)
			form.save()
			messages.success(request, f'success')
			return redirect('profile') ###
	else:
		form = UserDataForm()
	return render(request, 'user/profile.html', {'form':form})

