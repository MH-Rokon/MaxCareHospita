from django.db import models
from django.contrib.auth.models import User
from patient.models import patient
class  specialization(models.Model):
    name =models.CharField(max_length=30)
    slug=models.SlugField(max_length=30)
    def __str__(self):
        return self.name


class designation(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.name


class availableTime(models.Model):
    time=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30)
    def __str__(self):
        return self.time

class doctor(models.Model):
    user =models.OneToOneField(User,on_delete= models.CASCADE)
    image =models.ImageField(upload_to="doctor/image")
    specialization=models.ManyToManyField(specialization)
    Designation=models.ManyToManyField(designation)
    availableTime=models.ForeignKey(availableTime,on_delete=models.CASCADE)
    fee=models.IntegerField()
    meet_link=models.CharField(max_length=100)
    def __str__(self):
        return self.user.last_name
    
STAR_CHOICES=[

    ('✪' ,'✪'),
    ('✪✪', '✪✪'),
    ('✪✪✪' ,'✪✪✪'),
    ('✪✪✪✪' ,'✪✪✪✪'),
    ('✪✪✪✪✪' ,'✪✪✪✪✪'),
    
]    
    
class review(models.Model):
    reviewer=models.ForeignKey(patient, on_delete=models.CASCADE)
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating =models.CharField( max_length=100,choices= STAR_CHOICES)
    def __str__(self):
        return  f"Patient : {self.reviewer.user.last_name};Doctor:{self.doctor.user.last_name}"
    






    
    
