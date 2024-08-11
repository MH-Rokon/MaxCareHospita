# views.py

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import doctor, specialization, designation

def doctor_list(request):
    doctors = doctor.objects.all()
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
        'all_specializations': all_specializations,
        'all_designations': all_designations,
        'selected_specialization': specialization_id,
        'selected_designation': designation_id,
    }
    return render(request, 'doctor.html', context)

# Detail view of a single doctor
def doctor_detail(request, doctor_id):
    doctor_obj = get_object_or_404(doctor, id=doctor_id)
    
    context = {
        'doctor': doctor_obj,
    }
    return render(request, 'detail.html', context)
