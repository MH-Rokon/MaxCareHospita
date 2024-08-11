from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PatientForm
from .models import patient

@login_required
def info(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            patient_instance = form.save(commit=False)
            patient_instance.user = request.user
            patient_instance.save()
            
    else:
        form = PatientForm()
    
    return render(request, 'createpatient.html', {'form': form})
