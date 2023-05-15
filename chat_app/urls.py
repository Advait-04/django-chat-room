from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("admin/", admin.site.urls),
]
