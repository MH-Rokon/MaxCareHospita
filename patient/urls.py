from django.urls import path
from .views import info

urlpatterns = [
    path('profile/',info, name='info'),
    # other URL patterns
]
