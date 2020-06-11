from django.db import models
from membership.models import Membership
# Create your models here.

class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_membership = models.ManyToManyField(Membership)

    def __str__(self):
        return  self.title

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,related_name="lesson")
    position = models.IntegerField()
    video = models.FileField(upload_to='videos/',null=True,blank=True)
    def __str__(self):
        return  self.title