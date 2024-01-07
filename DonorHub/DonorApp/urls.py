from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= "home"),
    path("all/", views.donor_info, name = "all"),
    path('search/', views.search, name = 'search'),
    path('alter/<int:donor_id>/', views.alter, name = 'alter'),
    path('add/', views.add, name = 'add'),
    path('remove/<int:donor_id>/', views.remove, name = 'remove'),
    path('login/', views.login_view, name='login'),
    path('landing/', views.landing_page_view, name='landing_page'),



]