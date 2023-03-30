from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#Modeller default id atanmasi yapiliyormus ve 1'er increment'i var.

class BlogModel(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    publishDate = models.CharField(max_length=50)
    views = models.CharField(max_length=50)
    publisherName = models.CharField(max_length=50)
    imageName = models.CharField(max_length=50)
    leadTitle = models.CharField(max_length=500,null=True,blank=True)
    blockQuote = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField()
    description2 = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.title}"









