from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     
     path('', views.service_view, name='service_view'),
     

    
]

