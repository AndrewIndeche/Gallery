from django.db import models

# Create your models here.
class Category(models.Model):
    '''
    model for categories
    '''
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    '''
    model for location of Pics
    '''
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
        
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    '''
    model for Images
    '''
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def delete_Image(self):
        self.delete()
