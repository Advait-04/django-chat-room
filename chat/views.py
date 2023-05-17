from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from chat.models import User, Room, Message

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


def home(request):
    home_dict = {"username": curr_user}

    return render(request, "home.html", home_dict)


def room(request, room):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    return render(
        request,
        "room.html",
        {"username": username, "room": room, "room_details": room_details},
    )


def checkview(request):
    print("hello")

    room = request.POST.get("room")
    username = curr_user

    if Room.objects.filter(name=room).exists():
        return redirect("/" + room + "/?username=" + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect("/" + room + "/?username=" + username)


def send(request):
    message = request.POST.get("message")
    room_id = request.POST.get("room_id")
    username = request.POST.get("username")
    room = request.POST.get("room")

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    return redirect("/" + room + "/?username=" + username)


def getmessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({"messages": list(messages.values())})
