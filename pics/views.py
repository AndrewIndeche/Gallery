from django.http  import HttpResponse
from django.shortcuts import render
from . models import Image, Location

# Create your views here.
def welcome(request):
    return render(request, 'index.html')
