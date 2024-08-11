from django.shortcuts import render
from .models import service  

def  service_view(request):
    services = service.objects.all()
    return render(request, 'service.html', {'services': services})
