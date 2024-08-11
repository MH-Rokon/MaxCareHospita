from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm, EditAppointmentForm
from doctor.forms import ReviewForm
from doctor.models import doctor,review
from patient.models import patient
from django.contrib import messages

@login_required
def appointment_create(request, doctor_id):
    doctor_instance = get_object_or_404(doctor, id=doctor_id)
    
    try:
        patient_instance = patient.objects.get(user=request.user)
    except patient.DoesNotExist:
        return HttpResponseBadRequest("User is not registered as a patient. Click on the profile and create your patient account first")

    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user, doctor=doctor_instance)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor_instance
            appointment.patient = patient_instance

            time = form.cleaned_data['time']
            if not is_time_slot_available(doctor_instance, time):
                return HttpResponseBadRequest('Selected time slot is not available. Please choose another time.')

            appointment.save()
            return redirect('success')
        else:
            print(form.errors)  # For debugging purposes
    else:
        form = AppointmentForm(user=request.user, doctor=doctor_instance)

    return render(request, 'create_appointment.html', {
        'form': form,
        'doctor_instance': doctor_instance,
        'patient_last_name': patient_instance.user.last_name,  # Fetch patient’s last name
    })

@login_required
def is_time_slot_available(doctor_instance, selected_time):
    return not Appointment.objects.filter(doctor=doctor_instance, time=selected_time).exists()

@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    return redirect('list')

@login_required
def success(request):
    appointments = Appointment.objects.filter(patient__user=request.user)
    return render(request, 'appointment_success.html', {'appointments': appointments})

@login_required
def list(request):
    appointments = Appointment.objects.filter(doctor__user=request.user)
    return render(request, 'appointment_list.html', {'appointments': appointments})

@login_required
def change_status(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = AppointmentForm(instance=appointment)
    
    context = {
        'form': form,
        'appointment': appointment,
    }
    return render(request, 'change_status.html', context)

@login_required
def edit_appointment(request, appointment_id):
    appointment_instance = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        form = EditAppointmentForm(request.POST, instance=appointment_instance)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EditAppointmentForm(instance=appointment_instance)

    return render(request, 'edit_appointment.html', {'form': form, 'appointment_instance': appointment_instance})

@login_required
def review(request, doctor_id):
    doctor_instance = get_object_or_404(doctor, id=doctor_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_instance = form.save(commit=False)
            # Fetch the patient object associated with the user
            try:
                patient_instance = patient.objects.get(user=request.user)
                review_instance.reviewer = patient_instance
            except patient.DoesNotExist:
                # Handle the case where the user is not a patient
                return redirect('success')

            review_instance.doctor = doctor_instance
            review_instance.save()
            return redirect('success')
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form, 'doctor': doctor_instance})
