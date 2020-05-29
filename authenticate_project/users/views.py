from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserDataForm
from .main import verify_and_send
import logging
from users.models import UserData
from users.models import Employee
from django.contrib.auth.models import User

# Create your views here.

logger = logging.getLogger(__name__)

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
	return render(request, 'users/register.html', {'form': form})

# TODO: replace this
def employee(request):
	# need to create a custom form
	if request.method == 'POST':
		form = UserDataForm(request.POST)
		if form.is_valid():
			# POC logic goes here
			#a = verify_and_send(form)
			#logger.info("AAAAAA {}".format(a))
			# if verify_and_send(form):
			# 	form.save()
			# 	messages.success(request, f'success')
			# 	return redirect('profile') ###
			# else:
			# 	print("NOT VALID")
			# 	form = UserDataForm(request.POST)
			# 	messages.error(request, 'profile not valid')
			# 	return redirect('profile') ###
			return redirect('profile')
	else:
		form = UserDataForm()
	return render(request, 'users/employee.html', {'form': form})

def reroute(request):
	return render(request, 'users/reroute.html')
#decorator that adds functionality saying you have to be logged in to see your profile -PROBABLY WONT NEED 

#TODO - Verify_and_send may only work with lower version of Django - need to look into this 
#depending on if you're an employer or employee you want to see different profiles
@login_required
def profile(request):
	# if UserData.form_completion ==False
	
	username = request.user.username
	print(username)
	print(request.user)
	posts = Employee.objects.get()
	print(posts)
	print('IVE REACHED HEAR')
	if posts.form_completion == False:
		print('form has not been filled in')
		if request.method == 'POST':

			form = UserDataForm(request.POST, request.FILES)
			if form.is_valid():
				print("reached")
				# TODO: POC logic goes here
				form.save()
				# if verify_and_send(form):
				# 	form.save()
				# 	messages.success(request, f'success')
				# 	return redirect('profile') ###
				# else:
				# 	form = UserDataForm(request.POST)
				# 	messages.error(request, f'profile not valid')
				# 	return redirect('profile') ###
				#NEED TO SET THIS USERS FORM COMPLETION FIELD TO TRUE
				posts.form_completion = True
				posts.save()
				print(Employee.objects.get().form_completion)
				return redirect('profile')
		else:
			form = UserDataForm()
		return render(request, 'users/profile.html', {'form':form})
	else:
		return render(request, 'users/profile-complete.html')

