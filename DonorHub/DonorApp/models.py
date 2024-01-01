from django.db import models

# Create your models here.

class DonorInfo(models.Model):
    Firstname = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    DOB = models.DateField()
