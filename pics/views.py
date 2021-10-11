from django.http  import HttpResponse
from django.shortcuts import render
from . models import Image, Location,Category

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    pictures = Image.get_all()
    locations = Location.objects.all()
    return render(request, 'gallery.html', {'pictures': pictures, 'locations':locations})

def search(request):
    if 'imagesearch' in request.GET and request.GET['imagesearch']:
        category = request.GET.get('imagesearch')
        searched_images  = Image.search_image(category)
        message = f'{category}'
    
        return render(request, 'search.html', {'message':message, 'results':searched_images})
    else:
        message = 'Please Search for an image category'
        return render(request, 'search.html', {'message':message})

def location(request,locale):
    picture = Image.filter_by_location(locale)
    print(images)
    return render(request, 'location.html', {'results':images})
