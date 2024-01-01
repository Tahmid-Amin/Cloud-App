from django.urls import path
from . import views

urlpatterns = [
    path("", views.donor_info, name = "home")
]