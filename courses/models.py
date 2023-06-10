from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    
    def __str__(self):
        return self.title
    
class Video(models.Model):
    caption = models.CharField(max_length=50)
    video = models.FileField(upload_to='tutorials')
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.caption
    
    class Meta:
        ordering = ['-added']

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    lecturer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(User, related_name='students', blank=True)
    books = models.ManyToManyField(Book, blank=True)
    tutorial = models.ManyToManyField(Video, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-updated', '-created']
    

    
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf_ass = models.FileField(upload_to='assingments/pdfs/')
    done = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
class Submit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pdf_sub = models.FileField(upload_to='submited/assingments/pdfs/')
    
    def __str__(self):
        return self.owner
    
class RegProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)
    registerd = models.BooleanField()
    
    def __str__(self) -> str:
        return self.name
    
class Registration(models.Model):
    profile = models.ForeignKey(RegProfile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    