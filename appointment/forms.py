from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_type', 'appointment_status', 'symptom', 'time']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        doctor = kwargs.pop('doctor', None)
        super().__init__(*args, **kwargs)
        if user and hasattr(user, 'patient'):
            self.instance.patient = user.patient
        if doctor:
            self.instance.doctor = doctor
        # Hide the patient and doctor fields
        self.fields['appointment_status'].widget = forms.HiddenInput()

class EditAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_type', 'appointment_status', 'symptom', 'time']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        doctor = kwargs.pop('doctor', None)
        super().__init__(*args, **kwargs)
        if user and hasattr(user, 'patient'):
            self.instance.patient = user.patient
        if doctor:
            self.instance.doctor = doctor
