from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#python3 makemigrations
# database - need to run python3 migrate whenever you change models



class UserData(models.Model):
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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    form_completion = models.BooleanField(default=False)
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField()
    recruiter_email = models.EmailField()