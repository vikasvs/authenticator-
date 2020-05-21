from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# database stuff is here
# Create your models here.
#need to run migration to make any changes - python3 manage.py makemigrations
#python3 manage.py sqlmigrate authenticate 0001
#^ gives us html code
#run python3 manage.py migrate after this

#each class is its own table in teh database
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #how to return data when querying for it in django shell - python3 manage.py shell
    def __str__(self):
        return self.title