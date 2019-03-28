from django.db import models
from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe


# Create your models here.


    
class Address(models.Model):
    
    Address               = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Address

class Images(models.Model):
    
    image = models.ImageField()
    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()) )
    image_tag.short_description = 'Images'
    image_tag.allow_tags = True




class finder(models.Model):
    Photo                  =  models.ImageField()
    Name                   =  models.CharField(max_length=105)
    Description            =  models.TextField()
    ContactNumber          =  models.CharField(max_length=11)
    status                 =  models.CharField(max_length=25,choices=[('active','Active'),('inactive','IN_Active')])
    Date_lost              =  models.DateTimeField()
    TrackImage             =  models.ForeignKey(Images,on_delete=models.CASCADE,blank=True)
  
    TrackAddress           =  models.ManyToManyField('Address',blank=True)
   
  

    
  

    def __str__(self):
        return self.Name


    




