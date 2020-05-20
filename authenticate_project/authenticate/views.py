from django.shortcuts import render
from django.http import HttpResponse

#random data -  simulating a database call
posts  = [
	{
		'author': 'vikas',
		'title': 'test',
		'content': 'temp',
		'date': '05/07'
	},
	{
		'author': 'krunool',
		'title': 'test2',
		'content': 'temp2',
		'date': '05/07'
	}
	

]

def home(request):
	context  = {
		'posts': posts 
	}
	#request, render page, data
	return render(request, 'authenticate/home.html', context)


def about(request):
    return render(request, 'authenticate/about.html', {'title': 'About'})