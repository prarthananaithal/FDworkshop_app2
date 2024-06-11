
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        fullname=self.first_name + self.last_name
        return fullname
