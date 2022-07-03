from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters=list('abcdefghjiklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('Numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('~!@#$%^&*()+')

    thepassword=''
    length=int(request.GET.get('length', 12))
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})
def about(request):
    return render(request, 'generator/about.html')
