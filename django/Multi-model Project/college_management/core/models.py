from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    usn = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50)
    sem = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)