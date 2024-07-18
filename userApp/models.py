from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Regular', 'Regular')
    )
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICE)
    address = models.TextField(max_length=1000, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Regular')

    def __str__(self):
        return self.username