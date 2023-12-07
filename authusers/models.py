from django.db import models
from django.contrib.auth.models import User



class Person(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255,default = '')
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10,default = 'Patient')
    def __str__(self):
        return self.username
    
class Patient(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
class Doctor(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
