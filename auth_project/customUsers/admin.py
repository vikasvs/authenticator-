from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Employee, Employer


admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Employer)
