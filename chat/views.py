from django.shortcuts import render, redirect
from django.http import HttpResponse
from chat.models import User

import random


# Create your views here.
curr_user = "adv#123"


def generate_code():
    number = random.randint(1000, 9999)
    return number


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.get(username=username, password=password)

        curr_user = user.username

    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        password = request.POST.get("password")
        username = f"{fname}#{generate_code()}"

        user = User(fname=fname, username=username, password=password)
        user.save()

        print(f"fname: {fname} user:{username} pass: {password}")

        return redirect("/demo-chat")

    return render(request, "signup.html")


def demo_chat(request):
    u = User.objects.all()

    user_dict = {
        "username": curr_user,
        "items": u,
    }

    return render(request, "demo-chat.html", user_dict)
