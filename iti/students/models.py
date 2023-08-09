from django.db import models
from django.shortcuts import reverse

# Create your models here.

"I need to create a new model class for student "
"""
    id , name , grade , image, absent  for the student 
"""
from tracks.models import  Track
class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField(default=10)
    absent = models.BooleanField(default=True)
    image = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True)
    ## this track property --> represent track object

    def __str__(self):
        return f"{self.name}"

    def get_edit_url(self):
        ## return with edit url students.
        return reverse('students.edit', args=[self.id])





