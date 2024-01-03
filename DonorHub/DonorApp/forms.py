from django import forms
from .models import DonorInfo

class DonorForm(forms.ModelForm):
    class Meta:
        model = DonorInfo
        fields = '__all__'  # Include all fields from the Donor model