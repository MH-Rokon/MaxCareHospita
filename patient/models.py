from django.db import models
from django.contrib.auth.models import User

class patient (models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='patient/image/')
    phone_no=models.CharField(max_length=12)
    def __str__(self):
        return self.user.last_name

