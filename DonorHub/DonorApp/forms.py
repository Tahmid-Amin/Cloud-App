from django import forms
from .models import DonorInfo

class DonorForm(forms.ModelForm):
    class Meta:
        model = DonorInfo
        fields = ['Firstname', 'Surname', 'DOB', 'city', 'gender', 'bloodtype', 'image']  # Include all fields from the Donor model