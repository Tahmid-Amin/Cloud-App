from django.shortcuts import render, redirect
from .models import DonorInfo
from .forms import DonorForm
# Create your views here.

def home(request):
    return render(request, 'homepage.html')

def donor_info(request):
    donor = DonorInfo.objects.all()  # Retrieve all donors from the database
    return render(request, 'donor_info.html', {'donor': donor})

def search(request):
    if request.method == 'POST':
        blood_type = request.POST.get('blood_type')  # Example: Search by blood type
        city = request.POST.get('city')

         # Filter donors based on the provided parameters
        if blood_type and city:
            donor = DonorInfo.objects.filter(bloodtype__icontains=blood_type, city__icontains=city)
        elif blood_type:
            donor = DonorInfo.objects.filter(bloodtype__icontains=blood_type)
        elif city:
            donor = DonorInfo.objects.filter(city__icontains=city)
        else:
            # If no filters are provided, return all donors
            donor = DonorInfo.objects.all()

        return render(request, 'search_results.html', {'donor': donor})

    return render(request, 'search.html')
        #donor = DonorInfo.objects.filter(bloodtype__iexact=blood_type)
        #return render(request, 'search_results.html', {'donor': donor})
   # return render(request, 'search.html')

def alter(request, donor_id):
    donor = DonorInfo.objects.get(pk=donor_id)
    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('search')  # Redirect to the search page after altering
    else:
        form = DonorForm(instance=donor)
    return render(request, 'alter.html', {'form': form, 'donor': donor})

def add(request):
    if request.method == 'POST':
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('search')  # Redirect to the search page after adding
    else:
        form = DonorForm()
    return render(request, 'add.html', {'form': form})

def remove(request, donor_id):
    donor = DonorInfo.objects.get(pk=donor_id)
    if request.method == 'POST':
        donor.delete()
        return redirect('search') 
    return render(request, 'remove.html', {'donor': donor})

def login_view(request):
    return render(request, 'login.html')

def landing_page_view(request):
    return render(request, 'landing_page.html')
#def home(request):
    #return HttpResponse('Hello world!')