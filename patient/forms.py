from django import forms
from .models import patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['image', 'phone_no']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['phone_no'].required = True
