from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (EmployeeSignUpForm, EmployerSignUpForm, EmployeeDataForm, EmployerDataForm, RecommendationForm, NoModelPersonRecommendationForm)
import logging
import os
from django.contrib.auth import get_user_model
from .models import Employee, User, Employer
from .main import verify_and_send
from django.conf import settings
from django.utils.safestring import mark_safe
from auth_project.auth_project.settings import MEDIA_URL

logger = logging.getLogger(__name__)
# Create your views here.


def register_employee(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'You can now login!')
            return redirect('login')
    else:
        form = EmployeeSignUpForm()
    return render(request, 'customUsers/register-employee.html', {'form': form})

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

#THIS COMMENT MAY MESS IT UP
def profile(request):
    return redirect('profile-data')
    #return render(request, 'customUsers/base.html')

 #### NOTE: IGNORE THIS #### - I think we can comment this but honestly cant remember
# def employee(request):
#     # need to create a custom form
#     if request.method == 'POST':
#         form = EmployeeDataForm(request.POST)
#         if form.is_valid():
#             # POC logic goes here
#             if verify_and_send(form):
#                 form.save()
#                 messages.success(request, f'success')
#                 return redirect('profile-data') ###
#             else:
#                 print("NOT VALID")
#                 form = EmployeeDataForm(request.POST)
#                 messages.error(request, 'profile not valid')
#                 return redirect('profile-data') ###
#             return redirect('profile-data')
#     else:
#         form = EmployeeDataForm()
#     return render(request, 'users/employee.html', {'form': form})

# def employer(request):
#     return render(request, 'customUsers/base.html')

def reroute(request):
    return render(request, 'customUsers/reroute.html')

@login_required
def profile_data(request):
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
                    # if verify_and_send(form):
                    form.save()
                    populateEmployee(request, form, empUser, username)
                    messages.success(request, f'success')
                    empUser.form_completion = True
                    empUser.save()
                    print(empUser.form_completion)
                    return redirect('profile-complete') 
            else:
                form = EmployeeDataForm()
            return render(request, 'customUsers/profile-data.html', {'form':form})
        else:
            print('WHAT THE JESUS ')
            return redirect('profile-redirect')
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
                    return redirect('profile-complete')
            else:
                form = EmployerDataForm()
            return render(request, 'customUsers/profile-data.html', {'form':form})
        else:
            #return render(request, 'customUsers/profile-complete.html')
            return redirect('profile-complete')
## NOTE: profile means page employer uses to input their initial information

global_curr_employee = None
def profilePage(request):
    #assuming redirect from profile passes the same request to here
    if request.user.is_employee:
        print('BIDDIE')
        username = request.user.username
        currUser = User.objects.get(username=username)
        employeeUser = Employee.objects.get(user = currUser)
        userOfferLetter = employeeUser.offer_letter_name
        print('Here is the users offer letter name')
        print(userOfferLetter)
        employeeRec = employeeUser.reccomendation
        if (employeeRec != 'No reccomendations yet!'):
            employeeRec += ' - {}'.format(employeeUser.manager_name)
        verified_status = employeeUser.offer_letter_is_verified
        print(employeeUser.reccomendation)
        print(employeeUser.offer_letter_is_verified)
        return render(request, 'customUsers/employee-profile.html', {'employeeUser': employeeUser,'link':userOfferLetter, 'rec': employeeRec, 'verified_status':verified_status })

    else:
       
        username = request.user.username
        currUser = User.objects.get(username=username)
        empUser = Employer.objects.get(user = currUser)
        employee_list = EmployeeEmployerUpdate(request, empUser)
        form = NoModelPersonRecommendationForm(request.POST, request.FILES)
        print(employee_list)
        if request.method == 'POST':
            form = NoModelPersonRecommendationForm(request.POST)
            if form.is_valid() and form.cleaned_data.get('name_of_employee') in [e.your_name for e in employee_list]:
                global global_curr_employee #
                global_curr_employee = form.cleaned_data.get('name_of_employee')
                return redirect('rec-redirect')
            else:
                form = NoModelPersonRecommendationForm(request.POST)
                messages.error(request, 'you are not authorized to recommend this person')
                return redirect('profile-complete')
        else:
            form = NoModelPersonRecommendationForm()
            #form = PRecommendation()
        return render(request, 'customUsers/profile-complete.html',{'employerUser': empUser,'employee_list': employee_list, 'form':form})

    # return render(request, 'customUsers/profile-complete.html', {'links': templist})
    # form = displayAssociatedEmployees(request.POST, request.FILES)
    
    #return render(request, 'customUsers/profile-complete.html', {'employerUser': empUser})







#redirect to individuals personalized data
#here we show user attributes like offer letter, and reccomendation 
#this is an employer view
# TODO: Need to set emplpyer offer_letter name equivalent
def RecommendationRedirect(request):
    username = request.user.username
    currUser = User.objects.get(username=username)
    employerUser = Employer.objects.get(user = currUser)
    form = RecommendationForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            print('entered valid loop')
            employeeUser = Employee.objects.get(user=User.objects.get(username=global_curr_employee))
            print(employeeUser.your_name)
            employerUser.offer_letter = employeeUser.offer_letter
            print(form.cleaned_data)
            print('the clean recc is {}', form.cleaned_data['reccomendation'])
            employeeUser.reccomendation = form.cleaned_data['reccomendation']
            print(employeeUser.reccomendation)
            employeeUser.offer_letter_is_verified = form.cleaned_data['offer_letter_validity']
            print(' the form is {}', form.cleaned_data['offer_letter_validity'])


            employeeUser.save()
            employerUser.save()
            return redirect('profile-complete')
    else:
        form = RecommendationForm()
        

    print("GLOBAL ",global_curr_employee)
    print("OBJECTS ", User.objects.all())
    currUser = User.objects.get(username=global_curr_employee)
    print(currUser)
    userOfferLetter = Employee.objects.get(user=currUser).offer_letter_name
    print("FILE URL: {}".format(userOfferLetter))
    return render(request, 'customUsers/rec-redirect.html', {'form':form, 'document':userOfferLetter})
    #return render(request, 'customUsers/rec-redirect.html', {'form':form})

#need to fix this so we share name of link TODO
def EmployeeEmployerUpdate(request, current_user):
    employee_list = []
    employees = Employee.objects.all()
    print("TO MATCH: ", current_user.your_email)
    for e in employees:
        print("MANAGER EMAIL: ",e.manager_email)
        if e.manager_email == current_user.your_email: # TODO: change this to name and email
            current_user.offer_letter = e.offer_letter
            current_user.reccomendation = e.reccomendation
            employee_list.append(e)
            print('fuck it up')
    return employee_list



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



def populateEmployee(request, form, current_user, username):
    print('populate employee data')



    current_user.your_name = form.cleaned_data['your_name']
    current_user.your_email = form.cleaned_data['your_email']
    current_user.company_name = form.cleaned_data['company_name']
    current_user.role = form.cleaned_data['role']
    #current_user.offer_letter = form.cleaned_data['offer_letter']
    print(os.path.basename(form.cleaned_data['offer_letter'].name))
    #ol = update_filename(username,form.cleaned_data['offer_letter'].name)
    form.cleaned_data['offer_letter'].name = username +  form.cleaned_data['offer_letter'].name
    print('YO DAWG WE GOT')
    print(form.cleaned_data['offer_letter'].name)
    name = form.cleaned_data['offer_letter'].name
    current_user.offer_letter_name = f'{MEDIA_URL}{name}'
    print(current_user.offer_letter_name)
    current_user.offer_letter = form.cleaned_data['offer_letter']
    current_user.recruiter_email = form.cleaned_data['recruiter_email']

    current_user.manager_name = form.cleaned_data['manager_name']
    current_user.manager_email = form.cleaned_data['manager_email']
    current_user.recruiter_name = form.cleaned_data['recruiter_name']
    
    
    current_user.form_completion = True
    current_user.save()
    #print("EMP OFFER_LETTER: {}".format(current_user.offer_letter.url))


    print('employee data below')
    print(current_user.your_name)
    print(current_user.form_completion)
    print(current_user.your_email)
    print(current_user.offer_letter)


def update_filename(username, filename):
    path = "upload/path/"
    format = username + filename
    print("NAME UPDATE A SUCCESS")
    print(format)
    print(type(format))
    file_data = []
    file_data.append(format)
    file_data.append(os.path.join(path, format))
    return file_data