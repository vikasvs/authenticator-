from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from customUsers.models import Employee, User, Employer, EmployeeData, EmployerData

class EmployeeSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

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
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

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
        #'offer_letter',
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
        #'offer_letter',
        'role',
        'company_name']
