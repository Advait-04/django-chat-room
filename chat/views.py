from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
username = "nil"
password = "nil"


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    username = request.POST.get("fname")
    password = request.POST.get("password")

    print(f"User: {username} and Pass: {password}")

    return render(request, "signup.html")
