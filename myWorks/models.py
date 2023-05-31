from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Message(models.Model):
    fullName = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    message = models.TextField(max_length=300,null=False, blank=False)

    def __str__(self):
        return self.message
    
class Works(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    technologies = models.CharField(max_length=200,null=False, blank=False)
    image = CloudinaryField('images', default=None)

    def __str__(self):
        return self.name