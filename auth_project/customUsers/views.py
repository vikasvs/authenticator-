from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (EmployeeSignUpForm, EmployerSignUpForm, EmployeeDataForm, EmployerDataForm, RecommendationForm, NoModelPersonRecommendationForm)
import logging
from django.contrib.auth import get_user_model
from .models import Employee, User, Employer
from .main import verify_and_send
from django.conf import settings

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

#THIS COMMENT MAY FUCK SHIT UP
def profile(request):
    return redirect('profile-data')
    return render(request, 'customUsers/base.html')

 #### NOTE: IGNORE THIS ####
def employee(request):
    # need to create a custom form
    if request.method == 'POST':
        form = EmployeeDataForm(request.POST)
        if form.is_valid():
            # POC logic goes here
            if verify_and_send(form):
                form.save()
                messages.success(request, f'success')
                return redirect('profile-data') ###
            else:
                print("NOT VALID")
                form = EmployeeDataForm(request.POST)
                messages.error(request, 'profile not valid')
                return redirect('profile-data') ###
            return redirect('profile-data')
    else:
        form = EmployeeDataForm()
    return render(request, 'users/employee.html', {'form': form})

def employer(request):
    return render(request, 'customUsers/base.html')

def reroute(request):
    return render(request, 'customUsers/reroute.html')

@login_required
def profile_data(request):
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
                    # if verify_and_send(form):
                    form.save()
                    populateEmployee(request, form, empUser)
                    messages.success(request, f'success')
                    empUser.form_completion = True
                    empUser.save()
                    print(empUser.form_completion)
                    return redirect('profile-complete') ###
                    # else:
                    # 	form = EmployeeDataForm(request.POST, request.FILES)
                    # 	messages.error(request, f'profile not valid')
                    # 	return redirect('profile') ###
                        #NEED TO SET THIS USERS FORM COMPLETION FIELD TO TRUE
                    #return redirect('profile')
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
        userOfferLetter = employeeUser.offer_letter.url
        employeeRec = employeeUser.reccomendation
        is_letter_verified = employeeUser.reccomendation[1]
        print("the letter is {}",is_letter_verified )
        return render(request, 'customUsers/employee-profile.html', {'employeeUser': employeeUser,'document':userOfferLetter, 'rec': employeeRec})

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
            #if form.is_valid() and form.cleaned_data.get('name') in [e.your_name for e in employee_list]:
                global global_curr_employee # TODO: get rid of this eventually, but maybe nah lmao
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
    userOfferLetter = Employee.objects.get(user=currUser).offer_letter.url
    return render(request, 'customUsers/rec-redirect.html', {'form':form, 'document':userOfferLetter})
    #return render(request, 'customUsers/rec-redirect.html', {'form':form})

def EmployeeEmployerUpdate(request, current_user):
    employee_list = []
    employees = Employee.objects.all()
    print("TO MATCH: ", current_user.your_email)
    for e in employees:
        print("MANAGER EMAIL: ",e.manager_email)
        if e.manager_email == current_user.your_email: # TODO: change this to name and email
            #I want to set ____________ offer letter == offer letter and comment == comment
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



def populateEmployee(request, form, current_user):
    print('populate employee data')


    current_user.your_name = form.cleaned_data['your_name']
    current_user.your_email = form.cleaned_data['your_email']
    current_user.company = form.cleaned_data['company_name']
    current_user.role = form.cleaned_data['role']
    current_user.offer_letter = form.cleaned_data['offer_letter']
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
    print(current_user.offer_letter)




# def writeReccomendation()

# def validateOfferLetter()






