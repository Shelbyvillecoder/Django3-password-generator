from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Hello there friend</h1>')

def home(request):
    return render(request, 'generator/home.html')

def about(request):
      return render(request, 'generator/about.html')    

def password(request):

    characters = list('abcdefghijklmnopqrstuvxwyz')
    numlist = list('0,1,2,3,4,5,6,7,8,9')
    specchars = list('!@#$%^&*()_')

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*'))

    thepw = ''
    for x in range(length):
        thepw += random.choice(characters)  

    

    return render(request, 'generator/password.html',{'password': thepw})    


