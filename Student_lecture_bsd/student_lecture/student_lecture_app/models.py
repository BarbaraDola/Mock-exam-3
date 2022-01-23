from django.db import models

# Create your models here.
class Student(models.Model):
    name =  models.CharField(max_length=64, unique=True)#string, max. 64 znaki, imię powinno być unikalne
    year_at_university =  models.IntegerField()#integer,
    is_active = models.BooleanField(default=True)# boolean, standardowa wartość True,



class Lecture(models.Model):
    name = models.CharField(max_length=64, unique=True)
    lecturer = models.CharField(max_length=64)


