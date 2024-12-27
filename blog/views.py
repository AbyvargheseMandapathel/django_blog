from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'home.html')

def login(request):
    
    #if method POST
    #extract username
    #extract password
    
    #autheticate user 
    
    #correct - dashboard.html
    #else - login.html
    
    return render (request, 'login.html')

def signup(request):
    return render (request, 'signup.html')