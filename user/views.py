from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserDataForm
from .main import verify_and_send
import logging
from user.models import UserData
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
	return render(request, 'user/register.html', {'form': form})

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
	return render(request, 'user/employee.html', {'form': form})

def reroute(request):
	return render(request, 'user/reroute.html')
#decorator that adds functionality saying you have to be logged in to see your profile -PROBABLY WONT NEED 

#TODO
#want to render the form initially, but after form is filled, want to show offer letter, profile name and such
@login_required
def profile(request):
	# if UserData.form_completion ==False
	posts = UserData.objects.all()
	print(posts)
	print('IVE REACHED HEAR')
	for post in posts:
		print('tgus')
		print(post.form_completion)
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
			return redirect('profile')
	else:
		form = UserDataForm()
	return render(request, 'user/profile.html', {'form':form})

