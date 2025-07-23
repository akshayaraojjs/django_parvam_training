from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) # username will be captured based on the current login
    created_at = models.DateTimeField(auto_now_add=True) # timestamp when the blog was created

    def __str__(self):
        return self.title