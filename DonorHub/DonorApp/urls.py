from django.urls import path
from . import views

urlpatterns = [
    path("", views.donor_info, name = "home"),

    path('search/', views.search, name = 'search'),
    path('alter/<int:donor_id>/', views.alter, name = 'alter'),
    path('add/', views.add, name = 'add'),
    path('remove/<int:donor_id>/', views.remove, name = 'remove'),
]