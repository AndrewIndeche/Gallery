from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category= Category(name='home')
        self.category.save_category()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location= Location(name='home')
        self.location.save_location()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
