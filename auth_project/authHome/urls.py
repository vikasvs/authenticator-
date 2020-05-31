from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='authenticate-home'),
    path('about/', views.about, name='authenticate-about'),
]