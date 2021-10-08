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
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    '''
    model for Images
    '''
    image_link = models.ImageField(upload_to='images/',default='404.jpg')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
    @classmethod
    def get_all(cls):
        '''
        method to retrieve all images
        '''
        pics = Image.objects.all()
        return pics

    @classmethod
    def get_image_by_id(cls, id):
        '''
        method to retrieve image by unique id
        '''
        retrieved = Image.objects.get(id = id)
        return retrieved

    @classmethod
    def search_image(cls, cat):
        '''
        method to search image by category
        '''
        retrieved = cls.objects.filter(category__name__contains=cat) #image assoc w/ this cat
        return retrieved #list of instances


    def save_image(self):
        self.save()

    def delete_Image(self):
        self.delete()

    def update_image(self, new_url):
        '''
        method to update an image's link
        '''
        try:
            self.image_link = new_url
            self.save()
            return self
        except self.DoesNotExist:
            print('Image you specified does not exist')
