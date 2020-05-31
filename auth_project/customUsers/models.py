from django.db import models
from django.db.models.signals import post_save
# Create your models here.


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    form_completion = models.BooleanField(default=False)
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField()
    recruiter_email = models.EmailField()

#need to add a field for proof of employment
class Employer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    form_completion = models.BooleanField(default=False)
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField()
    company = models.CharField(max_length=255)



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


#probably need to fix this when I create an employer
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Employee.objects.create(user = kwargs['instance'])
        
        
post_save.connect(create_profile, sender = User)