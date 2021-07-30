#import the httpResponse module

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

	#return HttpResponse('This is the homepage')
	return render(request, 'homepage.html')


def about(request):
	#return HttpResponse('Request received and response sent')

	return render(request, 'about.html')


