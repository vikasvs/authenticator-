from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='user-profile'),
    path('employee-profile', views.profilePage, name = 'profile-redirect')
]