from django.http  import HttpResponse
from django.shortcuts import render
from . models import Image, Location

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    pictures = Image.get_all()
    locations = Location.objects.all()
    return render(request, 'gallery.html', {'pictures': pictures, 'locations':locations})

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        res = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'results':res})
    else:
        message = 'You have not searched any term'
        return render(request, 'search.html', {'message':message})

def location(request,locale):
    images = Image.filter_by_location(locale)
    return render(request, 'location.html', {'results':images})
