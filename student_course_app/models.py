from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class ElectiveCourse(models.Model):
    name = models.CharField(max_length=100)
    duration_in_months = models.IntegerField(default = 6)

    
    def __str__(self):
        return self.name
    
# Many students can study many courses

class Student(models.Model):
    id = models.BigIntegerField(primary_key = True,null = False)
    name = models.CharField(max_length=32)
    courses = models.ManyToManyField(ElectiveCourse, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.name
