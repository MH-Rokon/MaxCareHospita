from django.db import models
from patient.models import patient
from doctor.models import doctor, availableTime

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]

APPOINTMENT_TYPES = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=APPOINTMENT_TYPES, max_length=10)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS, max_length=10, default="Pending")
    symptom = models.TextField()
    time = models.ForeignKey(availableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name}, Patient: {self.patient.user.first_name}"
