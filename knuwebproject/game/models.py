from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name