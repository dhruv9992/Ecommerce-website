from unicodedata import name
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('', views.index, name='user' ),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('Contact', views.contact, name='Contact'),
    
]