from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse_lazy
from . import forms
from .models import Contact
from . import models
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from  contact.models import Contact
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def contact(request):
    contact=models.Contact.objects.all()
    return render(request,'contact.html',{"data":contact})

