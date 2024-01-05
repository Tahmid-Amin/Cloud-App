from django.db import models

# Create your models here.

class DonorInfo(models.Model):
     GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
     ]
     BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
     ]
     Firstname = models.CharField(max_length=100)
     Surname = models.CharField(max_length=100)
     DOB = models.DateField()
     city = models.CharField(max_length=100, default='london')
     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
     bloodtype = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, default='O+')
     image = models.ImageField(upload_to='donor_images', blank=True, null=True)
