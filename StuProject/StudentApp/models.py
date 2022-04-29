from django.db import models

class Student(models.Model):
    stu_id = models.IntegerField()
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    college = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

