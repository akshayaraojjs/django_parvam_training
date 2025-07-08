from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('User', 'User'),
)

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
]

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=10, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')

    def __str__(self):
        return self.username