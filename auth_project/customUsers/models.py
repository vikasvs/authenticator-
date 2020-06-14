from django.db import models
from django.db.models.signals import post_save
# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


    #tmp = models.BooleanField(default=False)


class EmployerData(models.Model):
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField()
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    form_completion = models.BooleanField(default = False)

class EmployeeData(models.Model):
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField()
    offer_letter = models.FileField(upload_to="documents/")
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=255)
    manager_email = models.EmailField()
    recruiter_name = models.CharField(max_length=255)
    recruiter_email = models.EmailField()
    form_completion = models.BooleanField(default = False)


class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    form_completion = models.BooleanField(default=False)

    your_name = models.CharField(max_length=255)
    your_email = models.EmailField()

    
    role = models.CharField(max_length=255, default = 'null')
    company_name = models.CharField(max_length=255, default = 'null')
    manager_name = models.CharField(max_length=255, default = 'null')
    manager_email = models.EmailField(default = 'null')
    recruiter_name = models.CharField(max_length=255, default = 'null')
    recruiter_email = models.EmailField(default = 'null')

    offer_letter = models.FileField(upload_to="documents/", default = 'null') # NOTE: filefield should auto generate a url to use
    reccomendation = models.CharField(max_length=255, default='No reccomendations yet!')
    offer_letter_is_verified = models.BooleanField(default=False)

#need to add a field for proof of employment
class Employer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    form_completion = models.BooleanField(default=False)
    
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField()
    
    role = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255)

    offer_letter = models.FileField(upload_to="documents/", null=True)
    reccomendation = models.CharField(max_length=255,default='No reccomendations yet!')

    # list of associated employees, every time the form is submitted, emplUser.employees.add(form.username)
    

"""
comment form
employee name 
involving some 
"""


#probably need to fix this when I create an employer
# def create_employee_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = Employee.objects.create(user = kwargs['instance'])
        
# def create_employer_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = Employer.objects.create(user = kwargs['instance'])

# post_save.connect(create_employee_profile, sender = User)
# post_save.connect(create_employer_profile, sender = User)