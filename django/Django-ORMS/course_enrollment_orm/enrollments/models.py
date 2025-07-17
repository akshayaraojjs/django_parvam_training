from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.title}"

class Student(models.Model):
    GENDER_CHOICES = [
                      ('M', 'Male'), 
                      ('F', 'Female'), 
                      ('O', 'Other')
                      ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, choices=[
        ('A+', 'Excellent'), ('A', 'Good'), ('B+', 'Fair'), ('B', 'Average'), ('C', 'Poor'), ('F', 'Fail')
    ])
    enrolled_on = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"