

from django.db import models

class Center(models.Model):
    id = models.AutoField(primary_key=True)
    centername = models.CharField(max_length=100)

    def __str__(self):
        return self.centername


class UserProfile(models.Model):
    registration_number = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100, default="")
    mothername = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    phone = models.CharField(max_length=10, default="")
    whatsapp = models.CharField(max_length=10, default="")
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    medium = models.CharField(max_length=10, choices=[('EN', 'English'), ('ML', 'Malayalam')], default='EN')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
