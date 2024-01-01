from django.shortcuts import render, HttpResponse
from .models import DonorInfo
# Create your views here.

def donor_info(request):
    donors = DonorInfo.objects.all()  # Retrieve all donors from the database
    return render(request, 'donor_info.html', {'donors': donors})

#def home(request):
    #return HttpResponse('Hello world!')