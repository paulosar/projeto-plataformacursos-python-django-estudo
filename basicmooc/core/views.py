from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def home(request):
    #return HttpResponse('hello world')
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')