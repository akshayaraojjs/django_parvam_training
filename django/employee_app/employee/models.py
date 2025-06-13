from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name