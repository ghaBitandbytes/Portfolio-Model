from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    about = models.TextField()
    education = models.CharField(max_length=255)
    skills = models.TextField()
    #profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True) #blank and null set to true in case if proifle picture do not upload in any case  
    profile_image = CloudinaryField('image', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#tells django what name to hsow in amdin  and in console  .without thiis, it just show onjects ..using str , user  can see stirng represntaion of object 
    def __str__(self):
        return self.name #can see name field of every object becaue of __str__method