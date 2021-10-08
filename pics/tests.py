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

class ImageTestClass(TestCase):
    '''
    test method to create Image instances called before all tests
    '''
    def setUp(self):
        self.category = Category(name='testing')
        self.category.save_category()

        self.location = Location(name='Nairobi')
        self.location.save_location()

        self.image_test = Image(id=1, name='image', description='lorem ipsum', category=self.category, location=self.location)
        self.image_test.save_image()

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_delete_Image(self):
        self.image_test.delete_Image()
        image = Image.objects.all()
        self.assertTrue(len(image) == 0)

    def test_update_image(self):
        update_test = self.image_test.update_image('images/h11.jpg')
        self.assertEqual(update_test.image_link, 'images/h11.jpg')

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)
