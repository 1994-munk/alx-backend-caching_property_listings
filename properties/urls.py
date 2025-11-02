from django.urls import path
from . import views

urlpatterns = [
    path('properties/', property_list, name='property_list'),
]
