from django.shortcuts import render

# Create your views here.


def home(request):
	#request, render page, data
	return render(request, 'authHome/home.html')


def about(request):
    return render(request, 'authHome/about.html', {'title': 'About'})