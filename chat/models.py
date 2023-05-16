from django.db import models

# Create your models here.


class User(models.Model):
    fname = models.CharField(max_length=20)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"fname: {self.fname} username: {self.username} password {self.password}"
