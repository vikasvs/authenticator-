from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Employee, Employer, EmployeeData, EmployerData


admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register