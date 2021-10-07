from django.db import models

# Create your models here.
class Category(models.Model):
    '''
    model for categories
    '''
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Location(models.Model):
    '''
    model for location of Pics
    '''
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    '''
    model for Images
    '''
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')

    def __str__(self):
        return self.title
