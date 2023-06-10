from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    journalist = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        
        
class Comments(models.Model):
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-added']