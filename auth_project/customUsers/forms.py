from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from customUsers.models import Employee, User, Employer, EmployeeData, EmployerData

class EmployeeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        
        return user


class EmployerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.save()
        employer = Employer.objects.create(user=user)
        
        return user



class EmployeeDataForm(forms.ModelForm):
    class Meta:
        #fields shown usr, email, password, pwd convifrmation
        model = EmployeeData
        fields = ['your_name',
        'your_email',
        'offer_letter',
        'role',
        'company_name',
        'manager_name',
        'manager_email',
        'recruiter_name',
        'recruiter_email']



class EmployerDataForm(forms.ModelForm):
    class Meta:
        #fields shown usr, email, password, pwd convifrmation
        model = EmployerData
        fields = ['your_name',
        'your_email',
        'role',
        'company_name']


class RecommendationForm(forms.Form):
    reccomendation = forms.CharField(label='Write a brief recommendation speaking to this candidates skills and qualifications below', max_length=400)
    offer_letter_validity = forms.BooleanField(label='Is the offer letter below the offer letter your company authorized?',required=True) 

class NoModelPersonRecommendationForm(forms.Form):
    name_of_employee = forms.CharField(label='Which employee would you like to verify?', max_length=100)