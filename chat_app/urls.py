from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("demo-chat", views.demo_chat, name="demo-chat"),
    path("home", views.home, name="home"),
    path("<str:room>/", views.room, name="room"),
    path("getmessages/<str:room>/", views.getmessages, name="getmessages"),
    path("checkview", views.checkview, name="checkview"),
    path("send", views.send, name="send"),
]
