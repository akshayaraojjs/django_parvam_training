from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=10)
    branch = models.CharField(max_length=20)
    sem = models.IntegerField()
    book_name = models.CharField(max_length=50)
    isbn_number = models.IntegerField(unique=True)
    author_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name