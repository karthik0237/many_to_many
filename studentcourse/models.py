
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True

class ElectiveCourse(BaseModel):
    course_id = models.CharField(primary_key=True,max_length=32)
    name = models.CharField(max_length=32,unique = True)
    duration_in_months = models.IntegerField(default = 6)
    active = models.BooleanField(default = True)

    
    def __str__(self):
        return self.name
    
# Many students can study many courses

class Student(BaseModel):
    id_no = models.BigIntegerField(primary_key = True,null = False)
    name = models.CharField(max_length=32)
    courses = models.ManyToManyField(ElectiveCourse)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

