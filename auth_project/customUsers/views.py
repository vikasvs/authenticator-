from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployeeSignUpForm, EmployerSignUpForm, EmployeeDataForm, EmployerDataForm
import logging
from django.contrib.auth import get_user_model
from .models import Employee, User, Employer
from .main import verify_and_send

logger = logging.getLogger(__name__)
# Create your views here.


def register(request):
	if request.method == 'POST':
		form = EmployeeSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			#username = form.cleaned_data.get('username')
			messages.success(request, f'You can now login!')
			return redirect('login')
	else:
		form = EmployeeSignUpForm()
	return render(request, 'customUsers/register.html', {'form': form})

def register_employer(request):
	if request.method == 'POST':
		form = EmployerSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			#username = form.cleaned_data.get('username')
			messages.success(request, f'You can now login!')
			return redirect('login')
	else:
		form = EmployerSignUpForm()
	return render(request, 'customUsers/register-employer.html', {'form': form})

def profile(request):
	return render(request, 'customUsers/base.html')

def employee(request):
	# need to create a custom form
	if request.method == 'POST':
		form = EmployeeDataForm(request.POST)
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
		form = EmployeeDataForm()
	return render(request, 'users/employee.html', {'form': form})

def employer(request):
	return render(request, 'customUsers/base.html')

def reroute(request):
	return render(request, 'customUsers/reroute.html')

@login_required
def profile(request):
	# if UserData.form_completion ==False
	if request.user.is_employee:
		username = request.user.username
		print(username)
		currUser = User.objects.get(username=username)
		print(currUser)
		empUser = Employee.objects.get(user = currUser)
		formStatus = empUser.form_completion

		print(formStatus)
		print('IVE REACHED HEAR')
		if formStatus == False:
			print('form has not been filled in')
			if request.method == 'POST':

				form = EmployeeDataForm(request.POST, request.FILES)
				if form.is_valid():
					print("reached")
						# TODO: POC logic goes here
					form.save()
					populateEmployee(request, form, empUser)
					# if verify_and_send(form):
					# 	form.save()
					# 	messages.success(request, f'success')
					# 	return redirect('profile') ###
					# else:
					# 	form = EmployeeDataForm(request.POST)
					# 	messages.error(request, f'profile not valid')
					# 	return redirect('profile') ###
						#NEED TO SET THIS USERS FORM COMPLETION FIELD TO TRUE
					empUser.form_completion = True
					empUser.save()
					print(empUser.form_completion)
					return redirect('profile')
			else:
				form = EmployeeDataForm()
			return render(request, 'customUsers/profile.html', {'form':form})
		else:
			return render(request, 'customUsers/profile-complete.html')
	else:
		username = request.user.username
		currUser = User.objects.get(username=username)
		empUser = Employer.objects.get(user = currUser)
		formStatus = empUser.form_completion
		print('Entered Profile')
		if formStatus == False:
			print('form has not been filled in')
			if request.method == 'POST':
				form = EmployerDataForm(request.POST, request.FILES)
				if form.is_valid():
					print("reached")
					form.save()
					populateEmployer(request, form, empUser)

					# TODO: need to redirect this to a different profile page altogether
					return redirect('profile')
			else:
				form = EmployerDataForm()
			return render(request, 'customUsers/profile.html', {'form':form})
		else:
			EmployeeEmployerUpdate(request, empUser)
			return render(request, 'customUsers/profile-complete.html')
	# else:
	# 	return render(request, 'users/profile-complete.html')


"""

Function that takes data from employee who listed employer's email and matches/shares it with the employer


"""
def EmployeeEmployerUpdate(request, current_user):
	employees = Employee.objects.all()
	print(current_user.your_email)
	for e in employees:
		print(e.recruiter_email)
		if e.recruiter_email == current_user.your_email:
			#I want to set ____________ offer letter == offer letter and comment == comment
			current_user.offer_letter = e.offer_letter
			current_user.reccomendation = e.reccomendation
			print('fuck it up')


def populateEmployer(request, form, current_user):
	print('populate employer data')


	current_user.your_name = form.cleaned_data['your_name']
	current_user.your_email = form.cleaned_data['your_email']
	current_user.company = form.cleaned_data['company_name']
	current_user.role = form.cleaned_data['role']
	current_user.form_completion = True
	current_user.save()


	print(current_user.your_name)
	print(current_user.form_completion)
	print(current_user.your_email)



def populateEmployee(request, form, current_user):
	print('populate employee data')


	current_user.your_name = form.cleaned_data['your_name']
	current_user.your_email = form.cleaned_data['your_email']
	current_user.company = form.cleaned_data['company_name']
	current_user.role = form.cleaned_data['role']
	current_user.manager_name = form.cleaned_data['manager_name']
	current_user.manager_email = form.cleaned_data['manager_email']
	current_user.recruiter_name = form.cleaned_data['recruiter_name']
	current_user.recruiter_email = form.cleaned_data['recruiter_email']

	current_user.form_completion = True
	current_user.save()



	print('employee data below')

	print(current_user.your_name)
	print(current_user.form_completion)
	print(current_user.your_email)




# def writeReccomendation()

# def validateOfferLetter()






