from django.db import models

# Create your models here.
class Candidate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    ]
    
    BRANCH_CHOICES = [
        ('CS', 'Computer Science'),
        ('EC', 'Electronics & Communication'),
        ('ME', 'Mechanical'),
        ('CV', 'Civil'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    address = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
class Registration(models.Model):
    DOMAIN_CHOICES = [
        ('Java', 'Java - Full Stack Web Development'),
        ('Python', 'Python - Full Stack Web Development'),
    ]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    internship_domains = models.CharField(max_length=50, choices=DOMAIN_CHOICES)
    date_enrolled = models.DateField(auto_now_add=True)