from django.db import models

# Create your models here.
class Branch(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ISE', 'Information Science'),
        ('ECE', 'Electronics & Communication'),
        ('EEE', 'Electrical & Electronics'),
    ]
    name = models.CharField(max_length=30, choices=BRANCH_CHOICES)
    short_form = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    age = models.IntegerField()
    sem = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    registration_date = models.DateField()

    def __str__(self):
        return self.name

class Admission(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    fees = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.fees}"