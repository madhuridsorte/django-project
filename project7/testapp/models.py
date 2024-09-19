from django.db import models

class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=30)
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    address = models.TextField()

