from django.urls import path
from . import views

urlpatterns = [
    path('take/<int:doctor_id>/', views.appointment_create, name='appointment'),
    path('success/', views.success, name='success'),
    path('list/', views.list, name='list'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('change-status/<int:appointment_id>/', views.change_status, name='change_status'),
    path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'), 
    path('review/<int:doctor_id>/', views.review, name='review'), 
]
