from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request , "Home.html")

def login(request):
    return render(request , "login.html")
    
def profile(request):
    return render(request , "profile.html")

def contact(request):
    return render(request , "contacts.html")

def dashboard(request):
    return render(request , "dashboard.html")

def signup(request):
    return render(request , "signup.html")

def report(request):
    return render(request , "report.html")

def location(request):
    return render(request , "location.html")