"""
WSGI config for auth_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
sys.path.insert(0,os.path.join(os.getcwd(), "auth_project/auth_project"))
sys.path.insert(0,os.path.join(os.getcwd(), "auth_project"))
print("CWD ******: {}".format(os.getcwd()))
print("FILE ABSPATH ******: {}".format(os.path.abspath(__file__)))


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_project.settings')

application = get_wsgi_application()
