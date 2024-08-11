from django.shortcuts import render
from doctor.models import doctor 
from service.models import service
from doctor.models import specialization, designation

def index(request):
    doctors = doctor.objects.all()
    services = service.objects.all()
    all_specializations = specialization.objects.all()
    all_designations = designation.objects.all()

    specialization_id = request.GET.get('specialization')
    designation_id = request.GET.get('designation')

    if specialization_id:
        doctors = doctors.filter(specialization__id=specialization_id)

    if designation_id:
        doctors = doctors.filter(Designation__id=designation_id)

    context = {
        'doctors': doctors,
        'services': services,
        'all_specializations': all_specializations,
        'all_designations': all_designations,
        'selected_specialization': specialization_id,
        'selected_designation': designation_id,
    }
    return render(request, 'index.html', context)
