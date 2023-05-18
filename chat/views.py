from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from chat.models import User, Room, Message

import random


def generate_code():
    number = random.randint(1000, 9999)
    return number


def index(request):
    return render(request, "index.html")


def login(request):
    err = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username, password=password)

        if user:
            curr_user = user
            return redirect("/home?username=" + username)

        else:
            user = User.objects.filter(username=username)
            if user:
                err = "Password doesnt match"
            else:
                err = "User does not exist"

    return render(request, "login.html", {"error": err})


def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        password = request.POST.get("password")
        username = f"{fname}_{generate_code()}"

        user = User(fname=fname, username=username, password=password)
        user.save()

        print(f"fname: {fname} user:{username} pass: {password}")

        return redirect("/home?username=" + username)

    return render(request, "signup.html")


def home(request):
    home_dict = {"username": request.GET.get("username")}

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
    room = request.POST.get("room")
    username = request.POST.get("username")

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

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    # return redirect("/" + room + "/?username=" + username)
    return HttpResponse("Message sent successfully")


def getmessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({"messages": list(messages.values())})
