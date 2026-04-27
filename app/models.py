from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    subcode = models.CharField(max_length=10)
    subname = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.subname


class Student(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    sem = models.IntegerField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name