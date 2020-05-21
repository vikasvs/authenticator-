from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# database stuff is here
# Create your models here.
#need to run migration to make any changes - python3 manage.py makemigrations

#each class is its own table in teh database
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title