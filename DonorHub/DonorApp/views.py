from django.shortcuts import render, HttpResponse
from .models import DonorInfo
# Create your views here.

def donor_info(request):
    donors = DonorInfo.objects.all()  # Retrieve all donors from the database
    return render(request, 'donor_info.html', {'donors': donors})

def search(request):
    return render(request, 'search.html')

def alter(request):
    return render(request, 'alter.html')

def add(request):
    return render(request, 'add.html')

def remove(request):
    return render(request, 'remove.html')


#def home(request):
    #return HttpResponse('Hello world!')