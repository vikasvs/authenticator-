from django.contrib import admin
from users.models import UserProfile
# Register your models here.

#shows data in django admin
admin.site.register(UserProfile)