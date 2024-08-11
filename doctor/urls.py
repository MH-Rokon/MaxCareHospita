from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     
     path('', views.doctor_list, name='doctor'),
     path('info/<int:doctor_id>/', views.doctor_detail, name='detail'),

    
]

