from django import forms
from .models import review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ['body', 'rating']
