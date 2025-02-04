from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=100,null=False,blank=False)
    subject = models.CharField(max_length=100,null=False,blank=False)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject}"
    

class Daily(models.Model):
    gratitude = models.TextField()
    field1 = models.TextField()
    affirmations = models.TextField()
    field2 = models.TextField()
    field3 = models.TextField()
    field4 = models.TextField()
    field5 = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name="Video Sahibi")

    def __str__(self):
        return f"{self.date}"
