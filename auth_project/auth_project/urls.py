"""auth_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from customUsers import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-employee/', user_views.register_employee, name = 'register-employee'),
    path('register-employer/', user_views.register_employer, name = 'register-employer'),
    path('reroute/', user_views.reroute, name = 'reroute'),
    #path('employee/', user_views.employee, name = 'employee'),
    path('login/', auth_views.LoginView.as_view(template_name='customUsers/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customUsers/logout.html'), name = 'logout'),

    path('profile-complete/', user_views.profilePage, name = 'profile-complete'),
    path('profile-data/', user_views.profile_data, name = 'profile-data'),
    path('rec-redirect/',user_views.RecommendationRedirect, name = 'rec-redirect'),
    path('', include('customUsers.urls')),
    path('', include('authHome.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
Profile complete should be renamed to profile
Profile should be renamed to profile-data
rec-redirect should be renamed to like employee-recomendation+

"""